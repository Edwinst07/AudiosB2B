import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Homologación Audios B2B")
root.geometry("500x300")

root.config(bg="#B0E0E6")

# img = Image.open("fondo.jpg")
# img = img.resize((400,400))
# img = ImageTk.PhotoImage(img)
# fondo_label = Label(root, image= img)
# fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

filename = ""

def buscarArchivo():
    global filename
    root.filename = filedialog.askopenfilename(title='Elige el archivo ', filetypes=(("txt files","*.txt"),("todos los archivos","*.*")))
    filename = root.filename
    file = os.path.split(filename)
    l = Label(root, text="Archivo a homologar: "+file[1])
    l.pack()

btn = Button(root, text='Cargar Archivo', command=buscarArchivo, fg="#FFFFFF", bg="blue")
                     #    1                       2                   3              4                      5                       6                   7               8             9                   10          11           12            13                  14                    15                16           17                            18                     19                  20                         21                     22                    23                            24               25                   26                     27         
valores =np.array(["DUO_TO_BA.wav","SERV PRO Y SERV ADMIN.wav","EQUIPOS.wav","DUO_VOZ PLUS_BA.wav","DUO_TRONCAL SIP_BA.wav","DUO_TO_TV.wav","DUO_TV_TO.wav","DUO_TV_BA.wav","HBOMAX_HOTPACK.wav","DTH.wav","RDSI PRI.wav","RDSI BRI.wav","NUMERO UNICO.wav","TELEFONIA PBX.wav","TRONCAL SIP.wav","VOZ PLUS.wav","CONMUTADOR VIRTUAL.wav","DUO_TELEFONIA PBX_BA.wav","CONECTIVIDAD.wav","INTERNET DEDICADO 1-1.wav","SERVICIOS CLOUD.wav","CYBER SECURITY.wav","HOSTING BASES DE DATOS.wav","MAIL HOSTING.wav","HOSTING DEDICADO.wav","WEB HOSTING.wav","DUO_BA_BA.wav" ])
        #         1         2              3               4             5             6              7             8              9                   10              11              12              13             14              15                16                 17           18             19             20              21              22             23            24             25             26            27                                                                                                                              
homol = ["DUOTOBA.wav","DUOTOBA.wav","DUOTOBA.wav", "DUOTOBA.wav","DUOTOBA.wav","DUOTOTV.wav","DUOTOTV.wav","DUOTVBA.wav","HBOMAXHOTPACK.wav","TELEVISION.wav","TELEFONIA.wav","TELEFONIA.wav","TELEFONIA.wav","TELEFONIA.wav","TELEFONIA.wav","TELEFONIA.wav","TELEFONIA.wav","TELEFONIA.wav","INTERNET.wav","INTERNET.wav","INTERNET.wav","INTERNET.wav","INTERNET.wav","INTERNET.wav","INTERNET.wav","INTERNET.wav","INTERNET.wav"]

def buscarOffice365(lineas):
    #listRegistrosEliminar = []
    for i in lineas:
        str = "".join(i)
        strs =str.split(";")
        for c in strs:
            if(c == "OFFICE 365.wav"):
                indiceLinea = lineas.index(i)
                #indice = int(indiceLinea[0])
                lineas.remove(lineas[indiceLinea])
    return lineas

def nuevalista(lineas):
    nuevaLista = []
    for li in lineas:
        nuevaLista.append(li)
    return nuevaLista

def homologacion(listaSinOffice,lineas):
    list = []
    list.append(lineas[0])
    for i in range(1, len(listaSinOffice),1):
        str = "".join(listaSinOffice[i])
        strs =str.split(";")
        for c in strs:

            for v in valores:
                if(c == v):
                    indice =np.where(v == valores)
                    valor = int(indice[0])
                    c = homol[valor]
            valor = ""
            if(c != "\n"):
                valor = c + ";"
            else:
                valor = c
            list.append(valor)
    return list

def main():
    #filename='C:/Users/Lenovo/Documents/Python/carganormal_b2b_013.txt'
    archivo = open(filename, "r")
    lineas =np.array(archivo.read().splitlines(True))
    nuevLista = nuevalista(lineas)
    buscarOffice = buscarOffice365(nuevLista)
    sinOffice = buscarOffice365(buscarOffice)
    homologado = homologacion(sinOffice,lineas)
    archivo.close()
    nombre = os.path.split(filename)
    parte = os.path.splitext(str(nombre[1]))
    archivo2 = open(parte[0]+"_modificado"+parte[1], "w")
    for i in homologado:
        archivo2.write(i)
    archivo2.close()

#main()
homologar = Button(root, text='Homologar archivo', command=main, fg="#FFFFFF", bg="blue")

btn.pack()

homologar.pack()
#fondo_label.pack()
root.mainloop()
