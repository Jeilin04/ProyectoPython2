import os
# import threading
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

os.system('cls') 

DatosRemitente = "Jeilin Crawford" #Sustituir con sus datos
rutaPC = "C:/CursoPythonGit/Pythonnivel1/Nivel_2/1_Tareas/Proyecto" #Sustituir con sus datos
ruta_completa2 = os.path.join(rutaPC, f"imagen_b.jpg") #Sustituir con sus datos

# Envía un correo electrónico rápido al destino indicado.
def sendQuickMail(subject:str, message:str, destination:str):

    print("Esto generará un QuickMail de confirmación")
    print("------------------------------------------ \n")
    Correo = input("Favor digite su correo \n") #Takechi21.88@gmail.com"
    Contraseña = input("Favor digite su contraseña de aplicación \n") #fophgvxjrbtckgvi

    mensaje = MIMEMultipart("alternative")
    mensaje["Subject"] = subject 
    mensaje["From"] = DatosRemitente 
    mensaje["To"] =  destination    

    mensajeU = MIMEText(message, "plain")
    mensaje.attach(mensajeU)
 
    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as conexion:
        conexion.starttls(context=context)
        conexion.login(Correo, Contraseña) 

        respuesta = conexion.sendmail(
            Correo, 
            destination,      
            mensaje.as_string()
            )
        print(respuesta, f"\n")

MensajeUsuario = "Se creo imagen deseada en la carpeta"

sendQuickMail("QuickMail-Comprobación", MensajeUsuario, "jeilinj@gmail.com")

#Envía un correo CON ADJUNTO a la dirección indicada
def sendAttachEmail(subject:str, message:str, destination:str, path:str):

    print("Esto generará un correo con el adjunto de la imagen generada")
    print("------------------------------------------------------------ \n")
    Correo = input("Favor digite su correo \n") #Takechi21.88@gmail.com"
    Contraseña = input("Favor digite su contraseña de aplicación \n") #fophgvxjrbtckgvi

    mensaje = MIMEMultipart("alternative")
    mensaje["Subject"] = subject 
    mensaje["From"] = DatosRemitente
    mensaje["To"] =  destination 

    with open(path, "rb") as img:
        image_dato = img.read()
        ArchivoImg = MIMEImage(image_dato, name=os.path.basename(path))
        mensaje.attach(ArchivoImg )

    mensajeU = MIMEText(message, "plain")
    mensaje.attach(mensajeU)
    
    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as conexion:
        conexion.starttls(context=context)
        conexion.login(Correo, Contraseña) 

        respuesta = conexion.sendmail(
            Correo, 
            destination,      
            mensaje.as_string()
            )
        print(respuesta)

MensajeUsuario = "Versión gris de imagen descargada de internet" 
sendAttachEmail("Imagen Gris de URL", MensajeUsuario, "jeilinj@gmail.com", ruta_completa2)
