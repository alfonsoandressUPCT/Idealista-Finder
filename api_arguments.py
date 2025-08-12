from geopy.geocoders import Nominatim
import requests

def api_arguments(variables):
    """
    Función para construir los argumentos necesarios para la búsqueda de pisos en la API de Idealista (formato multipart/form-data).
    """

    def obtener_codigo_iso(pais_nombre: str) -> str | None:
        url = f"https://restcountries.com/v3.1/name/{pais_nombre}"
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            if data:
                # data es una lista de países; cogemos el primero
                return data[0].get('cca2').lower()  # código ISO alfa-2
        return None

    def obtener_coordenadas(ciudad: str, pais: str) -> tuple[float, float] | None:
        geolocator = Nominatim(user_agent="idealista_finder")
        location = geolocator.geocode(f"{ciudad}, {pais}")
        if location:
            return (location.latitude, location.longitude)
        return None
    
    SEARCH_PARAMS = {}

    if str(variables["Tipo de Operación"]) == "Alquiler":
        SEARCH_PARAMS["operation"] = "rent"
    elif str(variables["Tipo de Operación"]) == "Venta":
        SEARCH_PARAMS["operation"] = "sale"
    elif str(variables["Tipo de Operación"]) == "Compartir":
        SEARCH_PARAMS["operation"] = "share"

    if str(variables["Tipo de Propiedad"]) == "Vivienda":
        SEARCH_PARAMS["propertyType"] = "homes"
    elif str(variables["Tipo de Propiedad"]) == "Habitación":
        SEARCH_PARAMS["propertyType"] = "rooms"
    elif str(variables["Tipo de Propiedad"]) == "Garajes":
        SEARCH_PARAMS["propertyType"] = "garages"
    elif str(variables["Tipo de Propiedad"]) == "Trasteros":
        SEARCH_PARAMS["propertyType"] = "storage"
    elif str(variables["Tipo de Propiedad"]) == "Oficinas":
        SEARCH_PARAMS["propertyType"] = "offices"
    elif str(variables["Tipo de Propiedad"]) == "Locales o Naves":
        SEARCH_PARAMS["propertyType"] = "commercial"
    elif str(variables["Tipo de Propiedad"]) == "Traspasos":
        SEARCH_PARAMS["propertyType"] = "transfers"
    elif str(variables["Tipo de Propiedad"]) == "Terrenos":
        SEARCH_PARAMS["propertyType"] = "land"
    elif str(variables["Tipo de Propiedad"]) == "Edificios":
        SEARCH_PARAMS["propertyType"] = "buildings"
    elif str(variables["Tipo de Propiedad"]) == "Vacacional":
        SEARCH_PARAMS["propertyType"] = "holiday"
    elif str(variables["Tipo de Propiedad"]) == "Obra Nueva":
        SEARCH_PARAMS["propertyType"] = "new_construction"

    coordenadas = obtener_coordenadas(variables['Ciudad'], variables['País'])
    if coordenadas:
        SEARCH_PARAMS["center"] = f"{coordenadas[0]},{coordenadas[1]}"
    SEARCH_PARAMS["distance"] = str(variables["Radio de Búsqueda"])
    SEARCH_PARAMS["numPage"] = '1'
    SEARCH_PARAMS["maxItems"] = '50'
    SEARCH_PARAMS["country"] = obtener_codigo_iso(variables["País"])

    SEARCH_PARAMS["bedrooms"] = str(variables["Habitaciones"])
    if variables["Baños"] == "":
        pass
    else:
        SEARCH_PARAMS["bathrooms"] = str(variables["Baños"])

    if variables["Precio Máximo"] == "":
        pass
    else:
        SEARCH_PARAMS["maxPrice"] = str(variables["Precio Máximo"])

    if variables["Precio Mínimo"] == "":
        pass
    else:
        SEARCH_PARAMS["minPrice"] = str(variables["Precio Mínimo"])

    if variables["Tamaño Mínimo"] == "":
        pass
    else:
        SEARCH_PARAMS["minSize"] = str(variables["Tamaño Mínimo"])

    if variables["Tamaño Máximo"] == "":
        pass
    else:
        SEARCH_PARAMS["maxSize"] = str(variables["Tamaño Máximo"])

    if variables["Ascensor"] == "Sin Ascensor":
        SEARCH_PARAMS["elevator"] = 'false'
    elif variables["Ascensor"] == 'Seleccionar':
        pass
    else:
        SEARCH_PARAMS["elevator"] = 'true'

    if variables["Garaje"] == "Sin Garaje":
        SEARCH_PARAMS["garage"] = 'false'
    elif variables["Garaje"] == 'Seleccionar':
        pass
    else:
        SEARCH_PARAMS["garage"] = 'true'

    # Otras configuraciones
    MAX_RESULTS = 50  # Número máximo de resultados a procesar

    return SEARCH_PARAMS, MAX_RESULTS