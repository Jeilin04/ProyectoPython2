# Instrucciones biblioteca *"ImgGrayMailJCWUCR"*

## Descripción

Esta bilioteca consiste en un conjunto de módulos que permiten:

- Descargar una imagen desde una URL deseada y visualizarla.
- Guardar la imagen en una dirección deseada de la PC.
- Convertir la imagen descargada en su versión en gris.
- Enviar 2 correos.
  - Uno tipo "QuickMail" informativo.
  - Otro con la imagen modificada como adjunto.

## Instalación

Para instalar el paquete de la biblioteca *"ImgGrayMailJCWUCR"*, es necesario seguir los siguientes pasos:

1. Crear la ruta o carpeta donde albergará el "main.py" del programa a ejecutar.
2. Crear el "main.py" genérico con el que ejecutará la biblioteca.
3. Activar/Abrir el _CMD_.
4. Ir a la ruta en la que creo el "main.py" y crear un entorno virtual (se recomienda este se llame _"env"_).

```terminal
python -m venv env
```
5. Activar el entorno virtual creado

```terminal
env\scripts\activate
```
6. Instalar la biblioteca con la siguiente línea de comando:

```terminal
pip install -i https://test.pypi.org/simple/ ImgGrayMailJCWUCR==0.0.1
```

7. Importar la biblioteca en el main (Ver el ejemplo que viene en la siguiente sección).
8. Ejecutar el main creado.

### Ejemplo código *"main.py"*.

```python
import sys
from ImgGrayMailJCWUCR.imagenes import showImageFromURL, downloadImageFromUrl, grayScaleImage
from ImgGrayMailJCWUCR.mymail import sendQuickMail, sendAttachEmail

def main(args):

    pass

if __name__ == '__main__':
    main(sys.argv)

```

## Referencias

Ruta repositorio Python:
<https://github.com/Jeilin04/ProyectoPython2>
