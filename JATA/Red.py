import random
import tkinter as tk
from tkinter import filedialog
import numpy as np



def Red():
    errorPatron = 0
    funcionActivacion = ""
    sumatoriaErroresPatron = 0
    errorPermitido = 0.1
    rataAprendizaje = 0.1
    numeroInteracciones = 0
    salidaSistema = [0] * 3
    patrones = []
    pesos=[]
    umbrales=[]
    erroresSalida=[0] * 3
    salidaOriginal=[]
 
    #calcular valor de las salidas
    get_output(salidaOriginal, salidaSistema, patrones, pesos, umbrales)

    #Calcular Error por salida
    output_error(erroresSalida,salidaOriginal,salidaSistema)

    #Calcular el error por patron
    pattern_error(erroresSalida, salidaOriginal, errorPatron)

    #Actualizar pesos
    update_weights(pesos, salidaOriginal, patrones, rataAprendizaje, erroresSalida)

    #Actualizar umbrales
    update_thresholds(umbrales, salidaOriginal, rataAprendizaje, erroresSalida)

    #Sumatoria y comprobacion de error
    error_checking(sumatoriaErroresPatron, errorPermitido)

    #Analisis de todos los patrones 
    analysis_of_all_patterns(salidaOriginal, salidaSistema, patrones, pesos, umbrales, erroresSalida, errorPatron, sumatoriaErroresPatron, rataAprendizaje, errorPermitido)

    #Repetir patrones segun el numero de interacciones
    patterns_according_to_interactions(salidaOriginal, salidaSistema, patrones, pesos, umbrales, erroresSalida, 
                                       errorPatron, sumatoriaErroresPatron, rataAprendizaje, errorPermitido, numeroInteracciones)
    
    #Cargar archivo de patrones
    file_upload(patrones, salidaOriginal)

    #Funcion de activacion
    activation_funcion(funcionActivacion, salidaSistema)

    #Creacion de pesos y umbrales aleatoriamente
    create_weights_thresholds(patrones, salidaOriginal, pesos, umbrales)


def get_output(salidaOriginal, salidaSistema, entradas, pesos, umbrales):
    print("calculando salida...")
    for i in range(len(salidaOriginal)):
        print("salida ", i)
        for j in range(len(entradas)):
            print("datos actuales:", entradas[j], pesos[j][i], umbrales[i])
            salidaSistema[i] += (entradas[j] * pesos[j][i]) 
            print("resultado: ", salidaSistema[i])
        salidaSistema[i] = salidaSistema[i] - umbrales[i]

def output_error(erroresSalida, salidaOriginal, salidaSistema):
    for i in range(len(salidaOriginal)):
        erroresSalida[i] = salidaOriginal[i] - salidaSistema[i]

def pattern_error(erroresSalida, salidaOriginal, errorPatron):
    for valor in erroresSalida:
        errorPatron = errorPatron + abs(valor)
    errorPatron = errorPatron / (len(salidaOriginal))
    return errorPatron

def update_weights(pesos, salidaOriginal, entradas, rataAprendizaje, erroresSalida):
    for i in range(len(salidaOriginal)):
        for j in range(len(entradas)):
            pesos[j][i] = pesos[j][i] + rataAprendizaje * erroresSalida[i] * entradas[j]

def update_thresholds(umbrales, salidaOriginal, rataAprendizaje, erroresSalida):
    for i in range(len(salidaOriginal)):
        umbrales[i] = umbrales[i] + rataAprendizaje * erroresSalida[i] * 1

def error_checking(sumatoriaErroresPatron, errorPermitido):
    if(sumatoriaErroresPatron <= errorPermitido):
        return True
    else:
        return False

def analysis_of_all_patterns(salidaOriginal, salidaSistema, patrones, pesos, umbrales, erroresSalida, errorPatron, sumatoriaErroresPatron, rataAprendizaje, errorPermitido):
    for i in range(len(patrones)):
        get_output(salidaOriginal, salidaSistema, patrones, pesos, umbrales)
        output_error(erroresSalida,salidaOriginal,salidaSistema)
        sumatoriaErroresPatron = pattern_error(erroresSalida, salidaOriginal, errorPatron) + sumatoriaErroresPatron
        update_weights(pesos, salidaOriginal, patrones, rataAprendizaje, erroresSalida)
        update_thresholds(umbrales, salidaOriginal, rataAprendizaje, erroresSalida)
    return error_checking(sumatoriaErroresPatron, errorPermitido)

def patterns_according_to_interactions(salidaOriginal, salidaSistema, patrones, pesos, umbrales, erroresSalida, 
                                       errorPatron, sumatoriaErroresPatron, rataAprendizaje, errorPermitido, numeroInteracciones):
    for i in range(numeroInteracciones):
        if (analysis_of_all_patterns(salidaOriginal, salidaSistema, patrones, pesos, umbrales, erroresSalida, errorPatron, sumatoriaErroresPatron, rataAprendizaje, errorPermitido) == True):
            return i
    return numeroInteracciones    

def file_upload(patrones, salidaOriginal):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    filename = file_path 
    matriz = np.loadtxt(filename)
    columnas = len(matriz[0])
    filas = len(matriz)

    for i in range(columnas):
        filaEntradas = []
        filaSalidas = []
        if(matriz[0][i] == 1):
            for j in range(1, filas):
                a = matriz[j][i]
                filaEntradas.append(a)
            patrones.append(filaEntradas)
        
        if(matriz[0][i] == 0):
            for j in range(1, filas):
                b = matriz[j][i]
                filaSalidas.append(b)
            salidaOriginal.append(filaSalidas)

def activation_funcion(funcionActivacion, salidaSistema):
    columnas = len(salidaSistema[0])
    filas = len(salidaSistema)
    if(funcionActivacion == "escalon"):
        for i in range(columnas):
            for j in range(1, filas):
                if(salidaSistema[j][i] < 0):
                    salidaSistema[j][i] == 0
                else:
                    salidaSistema[j][i] == 1

def create_weights_thresholds(patrones, salidaOriginal, pesos, umbrales):
    numeroEntradas = len(patrones)
    numeroSalidas = len(salidaOriginal)
    pesos = [[random.uniform(0, 1) for j in range(numeroSalidas)] for i in range(numeroEntradas)]
    umbrales = [random.uniform(0, 1) for j in range(numeroSalidas)]

        

    



