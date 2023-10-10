import os
import requests
from PIL import Image
from PIL import ImageOps
from io import BytesIO

os.system('cls') 

#Variables a sustituir por el programador a realizar pruebas, sería preferible sustiruirlas por input a futuro
URL = "https://images.pexels.com/photos/259881/pexels-photo-259881.jpeg?cs=srgb&dl=pexels-pixabay-259881.jpg&fm=jpg"
rutaPC = "C:/CursoPythonGit/Pythonnivel1/Nivel_2/1_Tareas/Proyecto" 

#Rutas para imagen previo y posterior a ajuste
ruta_completa = os.path.join(rutaPC, f"imagen_a.jpg")
ruta_completa2 = os.path.join(rutaPC, f"imagen_b.jpg")

#Descarga una imagen desde una URL y la muestra
def showImageFromURL(url:str): 

    mostrar = requests.get(url)
    with Image.open(BytesIO(mostrar.content)) as mi_imagen:
        mi_imagen.show()
    print("OK")

showImageFromURL(URL)

# Descarga una imagen y la guarda en la ruta indicada
def downloadImageFromUrl(url:str, path:str):

    guardar = requests.get(URL)
    with open(path, "wb") as archivo:
        archivo.write(guardar.content)
    print("OK")

downloadImageFromUrl(URL, ruta_completa)

# Convierte una imagen a blanco y negro
def grayScaleImage(path:str):

    img_gray1 = Image.open(path)
    img_gray2 = ImageOps.grayscale(img_gray1)
    img_gray2.save(ruta_completa2)  
    print("OK")

grayScaleImage(ruta_completa)


