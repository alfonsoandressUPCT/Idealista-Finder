import pandas as pd
import config
import seaborn as sns
import matplotlib.pyplot as plt
import os


def data_economy():
    """
    Función para analizar la economía de los datos extraidos por la API de Idealista.
    """

    output_dir = config.get_output_dir()
    variables = config.get_variables()

    def diagrama_barras(dataframe):
        """
        Función para crear diagramas de barras.
        """
        plt.figure(figsize=(12, 6))
        sns.barplot(data=dataframe, x=dataframe['Índice'], y=dataframe['Precio'], color='#e4f486')
        plt.title('Diagrama de Barras del Precio')
        plt.xlabel('Nº Inmueble')
        plt.ylabel('Precio (€)')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Barras/Diagrama de Barras - Precio | {variables['Ciudad']}.png')

        plt.figure(figsize=(12, 6))
        sns.barplot(data=dataframe, x=dataframe['Índice'], y=dataframe['Precio por Persona'], color='#e4f486')
        plt.title('Diagrama de Barras del Precio por Persona')
        plt.xlabel('Nº Inmueble')
        plt.ylabel('Precio (€)')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Barras/Diagrama de Barras - Precio por Persona | {variables['Ciudad']}.png')

        plt.figure(figsize=(12, 6))
        sns.barplot(data=dataframe, x=dataframe['Índice'], y=dataframe['Tamaño'], color='#e4f486')
        plt.title('Diagrama de Barras del Tamaño')
        plt.xlabel('Nº Inmueble')
        plt.ylabel('Tamaño (m²)')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Barras/Diagrama de Barras - Tamaño | {variables['Ciudad']}.png')

        plt.figure(figsize=(12, 6))
        sns.barplot(data=dataframe, x=dataframe['Índice'], y=dataframe['Precio por m²'], color='#e4f486')
        plt.title('Diagrama de Barras del Precio por m²')
        plt.xlabel('Nº Inmueble')
        plt.ylabel('Precio (€)')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Barras/Diagrama de Barras - Precio por Tamaño | {variables['Ciudad']}.png')

    def diagrama_cajas(dataframe):
        """
        Función para crear diagramas de cajas.
        """
        plt.figure(figsize=(12, 6))
        sns.boxenplot(data=dataframe, y=dataframe['Precio'], color='#e4f486')
        plt.title('Diagrama de Cajas del Precio')
        plt.ylabel('Precio (€)')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Cajas/Diagrama de Cajas - Precio | {variables['Ciudad']}.png')

        plt.figure(figsize=(12, 6))
        sns.boxenplot(data=dataframe, y=dataframe['Precio por Persona'], color='#e4f486')
        plt.title('Diagrama de Cajas del Precio por Persona')
        plt.ylabel('Precio (€)')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Cajas/Diagrama de Cajas - Precio por Persona | {variables['Ciudad']}.png')

        plt.figure(figsize=(12, 6))
        sns.boxenplot(data=dataframe, y=dataframe['Tamaño'], color='#e4f486')
        plt.title('Diagrama de Cajas del Tamaño')
        plt.ylabel('Tamaño (m²)')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Cajas/Diagrama de Cajas - Tamaño | {variables['Ciudad']}.png')

        plt.figure(figsize=(12, 6))
        sns.boxenplot(data=dataframe, y=dataframe['Precio por m²'], color='#e4f486')
        plt.title('Diagrama de Cajas del Precio por m²')
        plt.ylabel('Precio (€)')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Cajas/Diagrama de Cajas - Precio por Tamaño | {variables['Ciudad']}.png')

    def diagrama_lineas(dataframe):
        """
        Función para crear diagramas de líneas.
        """
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=dataframe, x=dataframe['Índice'], y=dataframe['Precio'], color='#e4f486')
        plt.title('Diagrama de Líneas del Precio')
        plt.xlabel('Nº Inmueble')
        plt.ylabel('Precio (€)')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Líneas/Diagrama de Líneas - Precio | {variables['Ciudad']}.png')

        plt.figure(figsize=(12, 6))
        sns.lineplot(data=dataframe, x=dataframe['Índice'], y=dataframe['Precio por Persona'], color='#e4f486')
        plt.title('Diagrama de Líneas del Precio por Persona')
        plt.xlabel('Nº Inmueble')
        plt.ylabel('Precio (€)')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Líneas/Diagrama de Líneas - Precio por Persona | {variables['Ciudad']}.png')

        plt.figure(figsize=(12, 6))
        sns.lineplot(data=dataframe, x=dataframe['Índice'], y=dataframe['Tamaño'], color='#e4f486')
        plt.title('Diagrama de Líneas del Tamaño')
        plt.xlabel('Nº Inmueble')
        plt.ylabel('Tamaño (m²)')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Líneas/Diagrama de Líneas - Tamaño | {variables['Ciudad']}.png')

        plt.figure(figsize=(12, 6))
        sns.lineplot(data=dataframe, x=dataframe['Índice'], y=dataframe['Precio por m²'], color='#e4f486')
        plt.title('Diagrama de Líneas del Precio por m²')
        plt.xlabel('Nº Inmueble')
        plt.ylabel('Precio (€)')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Líneas/Diagrama de Líneas - Precio por Tamaño | {variables['Ciudad']}.png')

    def histogramas(dataframe):
        """
        Función para crear histogramas.
        """
        plt.figure(figsize=(12, 6))
        sns.histplot(data=dataframe, x=dataframe['Precio'], kde=True, bins=20, color='#e4f486')
        plt.title('Histograma del Precio')
        plt.xlabel('Precio (€)')
        plt.ylabel('Frecuencia')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Histogramas/Histograma - Precio | {variables['Ciudad']}.png')

        plt.figure(figsize=(12, 6))
        sns.histplot(data=dataframe, x=dataframe['Precio por Persona'], kde=True, bins=20, color='#e4f486')
        plt.title('Histograma del Precio por Persona')
        plt.xlabel('Precio (€)')
        plt.ylabel('Frecuencia')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Histogramas/Histograma - Precio por Persona | {variables['Ciudad']}.png')

        plt.figure(figsize=(12, 6))
        sns.histplot(data=dataframe, x=dataframe['Tamaño'], kde=True, bins=20, color='#e4f486')
        plt.title('Histograma del Tamaño')
        plt.xlabel('Tamaño (m²)')
        plt.ylabel('Frecuencia')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Histogramas/Histograma - Tamaño | {variables['Ciudad']}.png')

        plt.figure(figsize=(12, 6))
        sns.histplot(data=dataframe, x=dataframe['Precio por m²'], kde=True, bins=20, color='#e4f486')
        plt.title('Histograma del Precio por m²')
        plt.xlabel('Precio (€)')
        plt.ylabel('Frecuencia')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Histogramas/Histograma - Precio por Tamaño | {variables['Ciudad']}.png')

    def medidas_descriptivas(dataframe):
        """
        Función para calcular y mostrar medidas descriptivas.
        """
        # Nos aseguramos de que el directorio output existe
        os.makedirs('output', exist_ok=True)

        # Creamos el archivo de medidas descriptivas
        with open(f'{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Medidas Descriptivas/Medidas Descriptivas | {variables['Ciudad']}.txt', 'w', encoding='utf-8') as file:
            file.write(f"Total Encontrados Inmuebles: {dataframe.shape[0]}\n")

            file.write(f"\nMedidas Descriptivas de Alojamientos en {variables['Ciudad']}. {variables['Habitaciones']} Personas\n")
            
            file.write(f"\tPrecio Medio: {dataframe['Precio'].mean():.2f} €\n")
            file.write(f"\tTamaño Medio: {dataframe['Tamaño'].mean():.2f} m²\n")
            file.write(f"\tPrecio por Persona Medio: {dataframe['Precio por Persona'].mean():.2f} €\n")
            file.write(f"\tPrecio por m² Medio: {dataframe['Precio por m²'].mean():.2f} €\n")

            file.write(f"\nMedianas Descriptivas de los Precios de Alojamientos en {variables['Ciudad']}. {variables['Habitaciones']} Personas\n")

            file.write(f"\tPrecio Medio: {dataframe['Precio'].median():.2f} €\n")
            file.write(f"\tTamaño Medio: {dataframe['Tamaño'].median():.2f} m²\n")
            file.write(f"\tPrecio por Persona Medio: {dataframe['Precio por Persona'].median():.2f} €\n")
            file.write(f"\tPrecio por m² Medio: {dataframe['Precio por m²'].median():.2f} €\n")

            file.write(f"\nDesviaciones Típicas de los Precios de Alojamientos en {variables['Ciudad']}. {variables['Habitaciones']} Personas\n")

            file.write(f"\tPrecio Medio: {dataframe['Precio'].std():.2f} €\n")
            file.write(f"\tTamaño Medio: {dataframe['Tamaño'].std():.2f} m²\n")
            file.write(f"\tPrecio por Persona Medio: {dataframe['Precio por Persona'].std():.2f} €\n")
            file.write(f"\tPrecio por m² Medio: {dataframe['Precio por m²'].std():.2f} €\n")

            file.write(f"\nRango de Precios de Alojamientos en {variables['Ciudad']}. {variables['Habitaciones']} Personas\n")

            file.write(f"\tPrecio Medio: {dataframe['Precio'].max() - dataframe['Precio'].min():.2f} €\n")
            file.write(f"\tTamaño Medio: {dataframe['Tamaño'].max() - dataframe['Tamaño'].min():.2f} m²\n")
            file.write(f"\tPrecio por Persona Medio: {dataframe['Precio por Persona'].max() - dataframe['Precio por Persona'].min():.2f} €\n")
            file.write(f"\tPrecio por m² Medio: {dataframe['Precio por m²'].max() - dataframe['Precio por m²'].min():.2f} €\n")

    df = pd.read_csv(f'{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis de Datos/Análisis de Datos | {variables['Ciudad']}. {variables['Habitaciones']} Personas.csv')

    diagrama_barras(df)
    diagrama_cajas(df)
    diagrama_lineas(df)
    histogramas(df)
    medidas_descriptivas(df)