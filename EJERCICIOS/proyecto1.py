import ee
import pandas as pd
import matplotlib.pyplot as plt
import folium
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileDownload

# Ruta al archivo JSON de autenticación de Google Earth Engine
credentials = service_account.Credentials.from_service_account_file(r'C:\Users\RYZEN 3\Desktop\datos.json\luminous-figure-388020-d56e0dc1d8a9.json')

# Inicializar Google Earth Engine con las credenciales
ee.Initialize(credentials=credentials)

# Definir la región de estudio (zona amazónica colombiana)
study_area = ee.Geometry.Rectangle([-75.0, -1.5, -66.0, 6.0])

# Obtener imágenes satelitales de interés (por ejemplo, imágenes de índice de vegetación NDVI)
def get_ndvi_images(start_year, end_year):
    collection = ee.ImageCollection('MODIS/006/MOD13Q1') \
        .filterDate(str(start_year), str(end_year)) \
        .filterBounds(study_area)
    ndvi_collection = collection.select('NDVI')
    return ndvi_collection

# Calcular el cambio en la cobertura forestal a lo largo del tiempo
def calculate_deforestation(start_year, end_year):
    ndvi_images = get_ndvi_images(start_year, end_year)
    initial_image = ee.Image(ndvi_images.first())
    final_image = ee.Image(ndvi_images.sort('system:time_start', False).first())
    deforestation = final_image.subtract(initial_image)
    return deforestation

# Calcular la tasa de deforestación entre 2015 y 2020
start_year = 2015
end_year = 2020
deforestation_rate = calculate_deforestation_rate(start_year, end_year)


# Calcular la tasa de deforestación en porcentaje
def calculate_deforestation_rate(start_year, end_year):
    deforestation = calculate_deforestation(start_year, end_year)
    deforestation_rate = deforestation.divide(255.0).multiply(100.0)
    return deforestation_rate.reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=study_area,
        scale=100,
        maxPixels=1e9
    ).values()


# Exportar la tasa de deforestación a Google Drive
task = ee.batch.Export.image.toDrive(
    image=deforestation_rate,
    description='deforestation_rate',
    folder='deforestation_analysis',
    scale=100,
    region=study_area
)
task.start()

# Esperar a que la tarea de exportación se complete
task_id = task.id
while task.status()['state'] in ['READY', 'RUNNING']:
    pass

# Descargar el archivo de Google Drive
def download_file_from_drive(file_id, file_path):
    drive_service = build('drive', 'v3', credentials=credentials)
    request = drive_service.files().get_media(fileId=file_id)
    with open(file_path, 'wb') as file:
        downloader = MediaFileDownload(file, request)
        done = False
        while not done:
            _, done = downloader.next_chunk()

# Descargar el archivo de tasa de deforestación desde Google Drive
file_id = task_id.split(':')[1]
file_path = r'C:\Users\RYZEN 3\Desktop\mapas.tif'
download_file_from_drive(file_id, file_path)

# Cargar los datos en un DataFrame de pandas
df = pd.read_csv(file_path)

# Obtener estadísticas básicas del DataFrame
stats = df.describe()

# Mostrar las estadísticas básicas
print(stats)

# Crear una gráfica de línea con la tasa de deforestación
plt.plot(df['year'], df['deforestation_rate'])
plt.xlabel('Año')
plt.ylabel('Tasa de Deforestación (%)')
plt.title('Tasa de Deforestación a lo largo del tiempo')
plt.grid(True)
plt.show()

# Calcular la media de la tasa de deforestación por año
mean_deforestation_rate = df.groupby('year')['deforestation_rate'].mean()

# Crear un nuevo DataFrame con la media de la tasa de deforestación por año
mean_df = pd.DataFrame({'Año': mean_deforestation_rate.index, 'Media de Deforestación (%)': mean_deforestation_rate.values})

# Mostrar la tabla con la media de la tasa de deforestación por año
print(mean_df)

# Crear una gráfica de barras con la media de la tasa de deforestación por año
plt.bar(mean_df['Año'], mean_df['Media de Deforestación (%)'])
plt.xlabel('Año')
plt.ylabel('Media de Deforestación (%)')
plt.title('Media de Deforestación por Año')
plt.grid(True)
plt.show()

# Crear un mapa interactivo con la tasa de deforestación
m = folium.Map(location=[-0.75, -70.0], zoom_start=7)

# Añadir la tasa de deforestación como capa en el mapa
folium.raster_layers.ImageOverlay(
    image=df['deforestation_rate'].values.reshape((df['year'].nunique(), -1)),
    bounds=[[study_area['coordinates'][0][1], study_area['coordinates'][0][0]],
            [study_area['coordinates'][2][1], study_area['coordinates'][2][0]]],
    colormap='YlOrRd',
    origin='upper'
).add_to(m)

# Mostrar el mapa interactivo
m
