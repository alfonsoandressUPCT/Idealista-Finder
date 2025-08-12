import folium
from folium.plugins import MarkerCluster
import pandas as pd
from api_arguments import api_arguments
import config

def data_map():
    """
    Función para crear un mapa interactivo con los datos obtenidos de la API de Idealista.
    """

    variables = config.get_variables()
    output_dir = config.get_output_dir()

    def obtener_coordenadas():
        """
        Función para obtener las coordenadas a través de los argumentos de la API de Idealista.
        """
        resultados = api_arguments(variables)

        SEARCH_PARAMS = resultados[0]

        coordenadas = SEARCH_PARAMS.get("center", "").split(",")

        latitud_ciudad = float(coordenadas[0])
        longitud_ciudad = float(coordenadas[1])

        return latitud_ciudad, longitud_ciudad

    latitud_ciudad, longitud_ciudad = obtener_coordenadas()

    mapa = folium.Map(location=[latitud_ciudad, longitud_ciudad], zoom_start=14)

    cluster = MarkerCluster().add_to(mapa)  # Agrupador de marcadores

    df = pd.read_csv(f'{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis de Datos/Análisis de Datos | {variables['Ciudad']}. {variables['Habitaciones']} Personas.csv')

    for index, row in df.iterrows():
        tooltip = f"Precio: {row['Precio']}\
                            <br> Precio por Persona: {row['Precio por Persona']}\
                            <br> Precio por m²: {row['Precio por m²']}\
                            <br> Tamaño: {row['Tamaño']}\
                            <br> Habitaciones: {row['Habitaciones']}\
                            <br> Baños: {row['Baños']}\
                            <br> Planta: {row['Planta']}\
                            <br> Garaje: {row['Garaje']}\
                            <br> Ascensor: {row['Ascensor']}\
                            <br> <a href='{row['url']}' target='_blank'>Ver alojamiento</a>"

        # Color según precio
        media_precio = df['Precio'].mean()

        if row['Precio'] < media_precio:
            color = 'green'
        elif row['Precio'] > media_precio:
            color = 'red'

        # Obtener coordenadas de vivienda
        coordenadas = row['Coordenadas'].split(',')
        latitud = float(coordenadas[0])
        longitud = float(coordenadas[1])

        folium.CircleMarker(
            location=[latitud, longitud],
            radius=6,
            color=color,
            fill=True,
            fill_opacity=0.7,
            popup=folium.Popup(tooltip, max_width=300)
        ).add_to(cluster)

        # Añadir leyenda personalizada al mapa
        legend_html = '''
        <div style="
            position: fixed; 
            bottom: 50px; left: 50px; width: 180px; height: 90px; 
            background-color: white; 
            border:2px solid grey; z-index:9999; font-size:14px;
            padding: 10px;
        ">
            <b>Leyenda de Precios</b><br>
            <i style="color:green;">●</i> Precio < Media<br>
            <i style="color:red;">●</i> Precio > Media
        </div>
        '''
        mapa.get_root().html.add_child(folium.Element(legend_html))

    output_dir = config.get_output_dir()
    mapa.save(f'{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Geográfico/Análisis Geográfico | {variables['Ciudad']}. {variables['Habitaciones']} Personas.html')