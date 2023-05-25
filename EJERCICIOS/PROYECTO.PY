import ee

# Inicializamos Google Earth Engine
ee.Authenticate()
ee.Initialize()

# Definimos la región de estudio (zona amazónica colombiana)
study_area = ee.Geometry.Rectangle([-75.0, -1.5, -66.0, 6.0])

# Obtenenemos imágenes satelitales de interés 
def get_ndvi_images(start_year, end_year):
    collection = ee.ImageCollection('MODIS/006/MOD13Q1') \
        .filterDate(str(start_year), str(end_year)) \
        .filterBounds(study_area)
    ndvi_collection = collection.select('NDVI')
    return ndvi_collection

# Calculamos el cambio en la cobertura forestal a lo largo del tiempo
def calculate_deforestation(start_year, end_year):
    ndvi_images = get_ndvi_images(start_year, end_year)
    initial_image = ee.Image(ndvi_images.first())
    final_image = ee.Image(ndvi_images.sort('system:time_start', False).first())
    deforestation = final_image.subtract(initial_image)
    return deforestation

# Calcular la tasa de deforestación en porcentaje
def calculate_deforestation_rate(start_year, end_year):
    deforestation = calculate_deforestation(start_year, end_year)
    deforestation_rate = deforestation.divide(255.0).multiply(100.0)
    return deforestation_rate

# Ejemplo de uso: calcular la tasa de deforestación entre 2015 y 2020
start_year = 2015
end_year = 2020
deforestation_rate = calculate_deforestation_rate(start_year, end_year)

# Imprimir información sobre la tasa de deforestación
print('Tasa de deforestación entre', start_year, 'y', end_year, ':')
print(deforestation_rate)

# Exportar la tasa de deforestación a Google Drive
task = ee.batch.Export.image.toDrive(
    image=deforestation_rate,
    description='deforestation_rate',
    folder='deforestation_analysis',
    scale=1000,
    region=study_area
)
task.start()
