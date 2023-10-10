import os
import threading
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

os.system('cls') 

#Saludo
print("¡Bienvenido! A continuación se generarán un QuickMail de confirmación de modificación de la imagen solicitada y un email con el archivo modificado como adjunto. \n")

#Variables a sustituir por el programador a realizar pruebas, sería preferible sustiruirlas por input a futuro
DatosRemitente = "Jeilin Crawford" 
rutaPC = "C:/CursoPythonGit/Pythonnivel1/Nivel_2/1_Tareas/Proyecto" 
ruta_completa2 = os.path.join(rutaPC, f"imagen_b.jpg") 

#Variables a solicitar al usuario según enunciado
Correo = input("Favor digite su correo \n") 
Contraseña = input("Favor digite su contraseña de aplicación \n") 

# Envía un correo electrónico rápido al destino indicado.
def sendQuickMail(subject:str, message:str, destination:str):

    #Recibe los parámetros indicados del correo (Título, remitente, receptor...)
    mensaje = MIMEMultipart("alternative")
    mensaje["Subject"] = subject 
    mensaje["From"] = DatosRemitente 
    mensaje["To"] =  destination    

    #Genera mensaje en cuerpo del correo
    mensajeU = MIMEText(message, "plain")
    mensaje.attach(mensajeU)
    
    #Inicializa TLS, pasa parámetro de usuario y envia email
    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as conexion:
        conexion.starttls(context=context)
        conexion.login(Correo, Contraseña) 
        conexion.sendmail(
            Correo, 
            destination,      
            mensaje.as_string()
            )

MensajeUsuario1 = "Se creo imagen deseada en la carpeta"

#Envía un correo CON ADJUNTO a la dirección indicada
def sendAttachEmail(subject:str, message:str, destination:str, path:str):

    #Recibe los parámetros indicados del correo (Título, remitente, receptor...)
    mensaje = MIMEMultipart("alternative")
    mensaje["Subject"] = subject 
    mensaje["From"] = DatosRemitente
    mensaje["To"] =  destination 

    #Abre la imagen con read binary y la adjunta al correo 
    with open(path, "rb") as img:
        image_dato = img.read()
        ArchivoImg = MIMEImage(image_dato, name=os.path.basename(path))
        mensaje.attach(ArchivoImg )

    #Genera mensaje en cuerpo del correo
    mensajeU = MIMEText(message, "plain")
    mensaje.attach(mensajeU)
    
    #Inicializa TLS, pasa parámetro de usuario y envia email
    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as conexion:
        conexion.starttls(context=context)
        conexion.login(Correo, Contraseña) 

        conexion.sendmail(
            Correo, 
            destination,      
            mensaje.as_string()
            )
        print("\n")

MensajeUsuario2 = "Versión gris de imagen descargada de internet" 

hilo1 = threading.Thread(target=sendQuickMail, args=("QuickMail-Comprobación", MensajeUsuario1, "jeilinj@gmail.com"))
hilo2 = threading.Thread(target=sendAttachEmail, args=("Imagen Gris de URL", MensajeUsuario2, "jeilinj@gmail.com", ruta_completa2))
hilo1.start()
hilo2.start()
hilo1.join()
hilo2.join()

print("Se generó un QuickMail de confirmación")
print("--------------------------------------- \n")
print("Se generó un correo con el adjunto de la imagen generada")
print("--------------------------------------------------------- \n")
