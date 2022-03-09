import xlrd
import pandas as pd
import numpy as np
import openpyxl

n_rival = input("Nombre equipo rival: ")
equipo = int(input("Goles equipo principal: "))
rival = int(input("Goles equipo rival: "))

notas_df=pd.read_excel('respuesta.xlsx')


f = open("documento.txt", "r")
lineas = f.read()
palabra = ""
lista_palabras = []
numeros = ["0","1","2","3","4","5","6","7","8","9"]
AhoraSi = True

for i in lineas:
    if i in numeros:
        palabra += i
    else:
        if palabra == '':
            pass
        else:
            if AhoraSi == True:
                palabra = int(palabra)
                lista_palabras.append(palabra)
                AhoraSi = False
            elif AhoraSi == False:
                AhoraSi = True
        palabra = ""

if equipo > rival:
    df = pd.DataFrame([[n_rival, "TRUE", "FALSE", "FALSE", equipo, rival, lista_palabras[0], lista_palabras[1], lista_palabras[2], lista_palabras[3], lista_palabras[4], lista_palabras[5]]], 
                columns=['a', 'b', 'c', 'd', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'])
elif rival > equipo:
    df = pd.DataFrame([[n_rival, "FALSE", "FALSE", "TRUE", equipo, rival, lista_palabras[0], lista_palabras[1], lista_palabras[2], lista_palabras[3], lista_palabras[4], lista_palabras[5]]], 
                columns=['a', 'b', 'c', 'd', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'])
elif equipo == rival:
    df = pd.DataFrame([[n_rival, "FALSE", "TRUE", "FALSE", equipo, rival, lista_palabras[0], lista_palabras[1], lista_palabras[2], lista_palabras[3], lista_palabras[4], lista_palabras[5]]], 
                columns=['a', 'b', 'c', 'd', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'])

df.to_excel('celta_data.xlsx')