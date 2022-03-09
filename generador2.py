import xlrd
import pandas as pd
import numpy as np
import openpyxl

f = open("documento.txt", "r")
lineas = f.read()
palabra = ""
lista_palabras = []
numeros = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18",
            "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32",
            "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46",
            "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60",
            "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74",
            "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88",
            "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100"]
separadores = [" ", "\n", "\t"]
categorias = ['CONTRICANTE', 'VICTORIA', 'EMPATE', 'DERROTA', 'GOLES_FAVOR', 'GOLES_CONTRA', 'FALTAS', 'AMARRILLAS', 'ROJAS', 'FUERA_LUGAR', 'ESQUINAS', 'SALVADAS', 'PENALES', 'H/V', 'POSECION%', 'YEAR', 'COMPETICION', 'JORNADA']
AhoraSi = True
lineas_2 = []
respuestas = []

for i in lineas:
    if i in separadores:
        lineas_2.append(palabra)
        palabra = ""
    else:
        palabra += i

for i in lineas_2:
    if i == "":
        pass
    else:
        if i in categorias:
            pass
        else:
            i = i.replace("\n", "")
            i = i.replace("\t", "")
            respuestas.append(i)

e=0
index = 0
writer = pd.ExcelWriter('respuesta.xlsx', engine='xlsxwriter')
#76
for i in range(0, 100):
    """df = pd.DataFrame([[respuestas[0+e], respuestas[1+e], respuestas[2+e], respuestas[3+e], respuestas[4+e], respuestas[5+e], respuestas[6+e], respuestas[7+e], respuestas[8+e], respuestas[9+e], respuestas[10+e], respuestas[11+e], respuestas[12+e], respuestas[13+e], respuestas[14+e], respuestas[15+e], respuestas[16+e], respuestas[17+e]]], 
                    columns=['CONTRICANTE', 'VICTORIA', 'EMPATE', 'DERROTA', 'GOLES_FAVOR', 'GOLES_CONTRA', 'FALTAS', 'AMARRILLAS', 'ROJAS', 'FUERA_LUGAR', 'ESQUINAS', 'SALVADAS', 'PENALES', 'H/V', 'POSECION%', 'YEAR', 'COMPETICION', 'JORNADA'
    ])"""
    rows = pd.DataFrame({'CONTRICANTE': respuestas[0+e],
                        'VICTORIA': respuestas[1+e],
                        'EMPATE': respuestas[2+e],
                        'DERROTA': respuestas[3+e],
                        'GOLES_FAVOR': respuestas[4+e],
                        'GOLES_CONTRA': respuestas[5+e],
                        'FALTAS': respuestas[6+e],
                        'AMARRILLAS': respuestas[7+e],
                        'ROJAS': respuestas[8+e],
                        'FUERA_LUGAR': respuestas[9+e],
                        'ESQUINAS': respuestas[10+e],
                        'SALVADAS': respuestas[11+e],
                        'PENALES': respuestas[12+e],
                        'H/V': respuestas[13+e],
                        'POSECION%': respuestas[14+e],
                        'YEAR': respuestas[15+e],
                        'COMPETICION': respuestas[16+e],
                        'JORNADA': respuestas[17+e],
    }, index=[index])
    e+=18
    index += 1
    if i == 0:
        rows.to_excel(writer, sheet_name="celta", index=True, header=True, startrow=index-1)
        index += 1
        rows.to_excel(writer, sheet_name="celta", index=True, header=False, startrow=index-1)
    else:
        rows.to_excel(writer, sheet_name="celta", index=True, header=False, startrow=index-1)
writer.save()
