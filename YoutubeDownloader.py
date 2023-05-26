from pytube import YouTube
#from tqdm import tqdm
import os

def EnterWait():
    input("Presione Enter para continuar...")

import os

def CompruebaRuta(ruta, RutaValida):
    if not os.path.exists(ruta):
        print("La ruta no existe")
        RutaValida[0] = False
        EnterWait()
    else:
        RutaValida[0] = True

def CompruebaLink(ruta, LinkValido):
    if not os.path.exists(ruta):
        print("El Link no existe")
        LinkValido[0] = False
        EnterWait()
    else:
        LinkValido[0] = True

def EnterWait():
    input("Presiona Enter para continuar...")

#def progress_callback(stream, chunk, bytes_remaining):
#   bytes_descargados = total_size - bytes_remaining
#   progreso = bytes_descargados / total_size * 100
#   pbar.update(progreso - pbar.n)



#Le pasamos el booleano en una lista para poder modificar su valor dentro de la función
RutaValida = [False]
LinkValido = [False]
Ruta = ""
link = ""
while not RutaValida[0]:
    os.system("cls")
    Ruta = input("Ingrese la ruta a la carpeta donde guardar los videos: ")
    CompruebaRuta(Ruta, RutaValida)

while not LinkValido[0]:
    os.system("cls")
    link = input("Introduce link de Youtube: ")
    CompruebaRuta(Ruta, LinkValido)

try:
    yt = YouTube(link)
    print(yt.title)
    stream = yt.streams.get_highest_resolution()
    total_size = stream.filesize
    nombre_archivo = yt.title + ".mp4"

    #with tqdm(total=total_size, unit='B', unit_scale=True) as pbar:
#            with open(ruta + nombre_archivo, 'wb') as file:
#            for chunk in stream.iter_content(chunk_size=1024):
#                if chunk:
 #                   file.write(chunk)
#                    pbar.update(len(chunk))


    stream.download(Ruta)
except Exception as ex:
    print(ex)
    EnterWait()
