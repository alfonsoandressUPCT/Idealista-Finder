# Idealista Finder

![Python](https://img.shields.io/badge/Python-100%25-blue)
![License](https://img.shields.io/github/license/alfonsoandressUPCT/Idealista-Finder?color=green)

## 📋 Descripción

Idealista Finder es una aplicación de escritorio que permite buscar, analizar y visualizar propiedades inmobiliarias disponibles en la plataforma Idealista. La herramienta realiza búsquedas personalizadas según los criterios del usuario y proporciona análisis estadísticos, económicos y geográficos de los resultados encontrados.

<p align="center">
  <img src="data/idealista_logo.png" alt="Idealista Finder Logo" width="200">
</p>

## 🔑 Características Principales

- **Búsquedas Personalizadas**: Filtra propiedades por ubicación, tipo de operación, características y más
- **Análisis Económico**: Visualizaciones estadísticas de precios, tamaños y otros parámetros relevantes
- **Visualización Geográfica**: Mapas interactivos que muestran la ubicación de las propiedades
- **Historial de Búsquedas**: Almacenamiento y recuperación de búsquedas anteriores
- **Interfaz Amigable**: GUI intuitiva desarrollada con CustomTkinter

## 🔧 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/alfonsoandressUPCT/Idealista-Finder.git

# Navegar al directorio
cd Idealista-Finder

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
# Crear un archivo .env con las siguientes variables:
# IDEALISTA_API_KEY=tu_api_key
# IDEALISTA_SECRET=tu_api_secret
# OPENWEATHERMAP_API_KEY=tu_api_key
```

## 📦 Dependencias

```txt
requests
customtkinter
python-dotenv
os
platform
Pillow
pandas
seaborn
matplotlib.pyplot
base64
time
folium
geopy
markdown
tkinterweb
```

## 🚀 Uso

1. Ejecuta el programa principal:
```bash
python main.py
```

2. En la interfaz de entrada, completa los campos requeridos:
   - Ciudad y país donde buscar
   - Tipo de operación (Venta, Alquiler, Compartir)
   - Tipo de propiedad (Vivienda, Habitación, etc.)
   - Radio de búsqueda (en metros)

3. Opcionalmente, especifica criterios adicionales:
   - Número de habitaciones y baños
   - Rango de precios
   - Tamaño de la propiedad
   - Características como ascensor o garaje

4. Haz clic en "Buscar" para iniciar la búsqueda.

5. Explora los resultados en la interfaz de salida, que incluye:
   - Análisis de datos tabulares
   - Visualizaciones económicas (gráficos, histogramas)
   - Mapa interactivo con las ubicaciones

## 📂 Estructura del Proyecto

### Módulos Principales

#### Interfaz de Usuario
- **`gui_input.py`**: Interfaz gráfica para capturar los parámetros de búsqueda
- **`gui_output.py`**: Interfaz para mostrar y navegar por los resultados
- **`gui_output_historical.py`**: Interfaz para acceder a búsquedas anteriores

#### Comunicación con API
- **`api_client.py`**: Cliente para autenticación y comunicación con la API de Idealista
- **`api_arguments.py`**: Construcción de parámetros para las solicitudes a la API
- **`api_request.py`**: Procesamiento de solicitudes y respuestas de la API

#### Análisis de Datos
- **`data_map.py`**: Generación de mapas interactivos con folium
- **`data_economy.py`**: Análisis económico y estadístico con pandas/seaborn

#### Utilidades
- **`config.py`**: Gestión centralizada de variables y configuraciones
- **`main.py`**: Punto de entrada principal y coordinación del flujo de ejecución

## 🔄 Flujo de Ejecución

1. **Entrada de Datos**
   - El usuario introduce los criterios de búsqueda a través de la GUI
   - Se validan los datos de entrada (ciudad, país, etc.)
   - Se crean las estructuras de directorios necesarias para almacenar resultados

2. **Procesamiento de la Búsqueda**
   - Se construyen los argumentos para la API de Idealista
   - Se realiza la autenticación OAuth2 con la API
   - Se ejecutan las solicitudes de búsqueda, paginando si es necesario
   - Se procesan los datos recibidos y se convierten a un DataFrame

3. **Análisis y Visualización**
   - Se generan estadísticas descriptivas (media, mediana, desviación estándar)
   - Se crean visualizaciones (diagramas de barras, cajas, líneas, histogramas)
   - Se construye un mapa interactivo con la ubicación de las propiedades

4. **Presentación de Resultados**
   - Se muestra la interfaz de resultados con múltiples pestañas
   - El usuario puede navegar entre diferentes análisis y visualizaciones
   - Se almacena la búsqueda en el historial para consultas futuras

## 📊 Tipos de Análisis

### Análisis de Datos
Tabla detallada con información de cada propiedad:
- Título y dirección
- Precio total y por persona
- Tamaño y precio por m²
- Características (habitaciones, baños, planta)
- Enlace a la propiedad

### Análisis Económico
Múltiples visualizaciones que incluyen:
- Diagramas de barras (precio, tamaño)
- Diagramas de cajas (distribución)
- Diagramas de líneas (tendencias)
- Histogramas (frecuencias)
- Medidas descriptivas (medias, medianas, desviaciones)

### Análisis Geográfico
Mapa interactivo que muestra:
- Ubicación de cada propiedad
- Código de colores según precio
- Información detallada al hacer clic
- Agrupación de marcadores (clustering)

## 👥 Autor

Alfonso Andrés - [@alfonsoandressUPCT](https://github.com/alfonsoandressUPCT)

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 🔑 Requisitos de API

Para utilizar Idealista Finder, necesitarás:
- Una clave de API de Idealista (para búsquedas de propiedades)
- Una clave de API de OpenWeatherMap (para validación de ciudades)

Estas credenciales deben configurarse en un archivo `.env` en la raíz del proyecto.