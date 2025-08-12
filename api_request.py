import pandas as pd
from api_client import IdealistaAPI
import config

def api_request(SEARCH_PARAMS, MAX_RESULTS):

    # Inicializar la API
    api = IdealistaAPI()
    
    # Realizar la búsqueda inicial
    results = api.search_properties(SEARCH_PARAMS)
    
    if not results or 'elementList' not in results:
        raise ValueError("No se encontraron resultados o la respuesta de la API es inválida.")
    
    # Procesar y mostrar resultados
    properties = results['elementList']
    total_pages = results.get('totalPages', 1)
    
    # Si hay más páginas y no hemos alcanzado el máximo de resultados
    current_page = 1
    while current_page < total_pages and len(properties) < MAX_RESULTS:
        current_page += 1
        
        params = SEARCH_PARAMS.copy()
        params['numPage'] = str(current_page)
        
        more_results = api.search_properties(params)
        if more_results and 'elementList' in more_results:
            properties.extend(more_results['elementList'])
        
        # Evitar sobrepasar el máximo de resultados
        if len(properties) >= MAX_RESULTS:
            properties = properties[:MAX_RESULTS]
            break
    
    # Crear un DataFrame para análisis con los campos específicos solicitados
    data = []
    for prop in properties:

        # Obtener datos básicos
        precio = prop.get('price', 0)
        habitaciones = prop.get('rooms', 1)  # Default a 1 para evitar división por cero
        
        # Calcular precios por persona
        precio_por_persona = precio / habitaciones if habitaciones > 0 else precio

        # Planta
        planta = prop.get('floor', 0)
        if planta == "bj":
            planta = 0

        # Verificar si hay garaje
        garaje = False
        if 'parkingSpace' in prop and isinstance(prop['parkingSpace'], dict):
            # Usar el campo directo de la API
            garaje = prop['parkingSpace'].get('hasParkingSpace', False)
        
        if garaje == True:
            garaje = 'Sí'
        else:
            garaje = 'No'

        # Verificar si hay ascensor
        ascensor = False
        if 'hasLift' in prop and isinstance(prop['hasLift'], bool):
            ascensor = prop['hasLift']

        if ascensor == True:
            ascensor = 'Sí'
        else:
            ascensor = 'No'

        # Exterior
        exterior = prop.get('exterior', False)
        if exterior == True:
            exterior = 'Sí'
        else:
            exterior = 'No'
        
        # Recopilar todos los datos
        data.append({
            'Título': prop.get('title', prop.get('address', 'Sin título')).title(),
            'Precio': precio,
            'Precio por Persona': round(precio_por_persona, 3),
            'Precio por m²': round(prop.get('priceByArea', 0), 3),
            'Tamaño': prop.get('size', 0),
            'Habitaciones': habitaciones,
            'Baños': prop.get('bathrooms', 0),
            'Planta': planta,
            'Garaje': garaje,
            'Ascensor': ascensor,
            'Dirección': prop.get('address', '').title(),
            'Coordenadas': f"{prop.get('latitude', '')},{prop.get('longitude', '')}",
            'Código de la Propiedad': prop.get('propertyCode', 'No disponible').title(),
            'url': prop.get('url', ''),
        })
    
    df = pd.DataFrame(data)

    df.insert(0, 'Índice', range(1, len(df) + 1))

    # Guardar resultados en CSV
    output_dir = config.get_output_dir()
    variables = config.get_variables()
    csv_filename = f'{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis de Datos/Análisis de Datos | {variables['Ciudad']}. {variables['Habitaciones']} Personas.csv'
    df.to_csv(csv_filename, index=False)