# **Instrucciones de Uso de Idealista Finder**

## **¿Qué Encontrarás en esta Aplicación?**

**Idealista Finder** es una herramienta diseñada para ayudarte a buscar propiedades inmobiliarias según tus criterios específicos. La ventana principal está dividida en tres secciones:

- **Parámetros Necesarios** (Panel Amarillo): Información esencial que debes completar para realizar cualquier búsqueda.
- **Parámetros Opcionales** (Panel Verde): Filtros adicionales para refinar tu búsqueda.
- **Realizar Búsqueda** (Panel Rosa): Sección con el botón para iniciar la búsqueda y otras opciones.

## **Parámetros Necesarios**

Estos campos deben completarse **obligatoriamente**:

### **Ciudad**
- Introduce el nombre de la ciudad donde deseas buscar propiedades.
- Debe ser un nombre de ciudad válido y existente.
- **Ejemplo:** "Madrid", "Barcelona", "Valencia".

### **País**
- Introduce el nombre del país donde se encuentra la ciudad.
- Debe ser un nombre de país válido y existente.
- **Ejemplo:** "España", "Francia", "Italia".

### **Tipo de Operación**
- Selecciona el tipo de transacción que te interesa.
- **Opciones Disponibles:**
    - Venta
    - Alquiler
    - Compartir

### **Tipo de Propiedad**
- Selecciona qué tipo de inmueble estás buscando.
- **Opciones Disponibles:**
    - Vivienda
    - Habitación
    - Garajes
    - Trasteros
    - Oficinas
    - Locales o Naves
    - Traspasos
    - Terrenos
    - Edificios
    - Vacacional
    - Obra Nueva

### **Radio de Búsqueda**
- Introduce la distancia (en metros) desde el centro de la ciudad.
- Debe ser un valor entre 0 y 10.000 metros.
- **Ejemplo**: "500" buscará propiedades en un radio de 500 metros desde el centro de la ciudad.

## **Parámetros Opcionales**

Estos campos son opcionales y te permiten filtrar con más precisión:

### **Habitaciones**
- Introduce el número exacto de habitaciones que deseas.
- Debe ser un número positivo.
- En caso de dejarlo en blanco, no se tendrá en cuenta a la hora de la búsqueda.
- **Ejemplo:** "2" buscará propiedades con exactamente 2 habitaciones.

### **Baños**
- Introduce el número mínimo de baños que deseas.
- Debe ser un número positivo si se especifica.
- En caso de dejarlo en blanco, no se tendrá en cuenta a la hora de la búsqueda.
- **Ejemplo:** "1" buscará propiedades con al menos 1 baño.

### **Precio Mínimo**
- Introduce el precio mínimo (en euros) que estás dispuesto a pagar.
- Debe ser un número positivo si se especifica.
- En caso de dejarlo en blanco, no se tendrá en cuenta a la hora de la búsqueda.
- **Ejemplo:** "100000" filtrará propiedades por encima de 100.000€.

### **Precio Máximo**
- Introduce el precio máximo (en euros) que estás dispuesto a pagar.
- Debe ser un número positivo si se especifica.
- En caso de dejarlo en blanco, no se tendrá en cuenta a la hora de la búsqueda.
- **Ejemplo:** "300000" filtrará propiedades por debajo de 300.000€.

### **Tamaño Mínimo**
- Introduce el tamaño mínimo (en metros cuadrados) que deseas.
- Debe ser un número positivo si se especifica.
- En caso de dejarlo en blanco, no se tendrá en cuenta a la hora de la búsqueda.
- **Ejemplo:** "60" buscará propiedades de al menos 60m².

### **Tamaño Máximo**
- Introduce el tamaño máximo (en metros cuadrados) que deseas.
- Debe ser un número positivo si se especifica.
- En caso de dejarlo en blanco, no se tendrá en cuenta a la hora de la búsqueda.
- **Ejemplo:** "120" buscará propiedades de hasta 120m².

### **Ascensor**
- Selecciona si deseas propiedades con o sin ascensor.
- **Opciones:**
    - Seleccionar (Sin Preferencia)
    - Con Ascensor
    - Sin Ascensor
- En caso de dejarlo en "Seleccionar", no se tendrá en cuenta a la hora de la búsqueda.

### **Garaje**
- Selecciona si deseas propiedades con o sin garaje.
- **Opciones:** 
    - Seleccionar (Sin Preferencia)
    - Con Garaje 
    - Sin Garaje
- En caso de dejarlo en "Seleccionar", no se tendrá en cuenta a la hora de la búsqueda.

## **Realizando la Búsqueda**

Una vez que hayas completado los campos necesarios y los opcionales que te interesen:

1. Haz clic en el botón **Buscar** para iniciar la búsqueda.
2. El sistema validará tus entradas para asegurarse de que son correctas:
   - Si hay algún error, aparecerá una ventana emergente con información sobre el problema.
   - Si todo es correcto, la aplicación comenzará a buscar propiedades según tus criterios.

## **Resultados**

Tras realizar la búsqueda, la aplicación creará una estructura de directorios en la carpeta "output" con los siguientes análisis:

- **Análisis de Datos:** Información general sobre las propiedades encontradas.
- **Análisis Económico:** Visualizaciones y estadísticas sobre precios (diagramas de barras, cajas, líneas, histogramas y medidas descriptivas).
- **Análisis Geográfico:** Mapas y distribución espacial de las propiedades.

Los resultados se guardarán en una carpeta con el nombre de la ciudad y el número de habitaciones especificado.

## **Notas Adicionales**

- Para obtener los mejores resultados, intenta ser específico en tus criterios de búsqueda.
- Si no encuentras resultados, prueba a ampliar el radio de búsqueda o reducir algunos filtros.
- La aplicación requiere conexión a internet para validar ciudades y países, así como para realizar las búsquedas.