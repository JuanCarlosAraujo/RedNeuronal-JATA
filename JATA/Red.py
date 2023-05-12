import random
import tkinter as tk
from tkinter import filedialog
import numpy as np



class Red():
    def __init__(self, rata, iteraciones,funActivacion,errorPermitido):

        self.errorPatron = 0
        self.funcionActivacion = funActivacion
        self.sumatoriaErroresPatron = 0
        self.errorPermitido = errorPermitido
        self.rataAprendizaje = rata
        self.numeroInteracciones = iteraciones
        self.salidaSistema = []
        self.patrones = []
        self.pesos=[]
        self.umbrales=[]
        self.erroresSalida=[]
        self.salidaOriginal=[]
        self.numeroEntradas = 0
        self.numeroSalidas = 0
 
    def get_output(self,entradas):
        print(self.pesos)
        salida= [0] * self.numeroSalidas
        for i in range(self.numeroSalidas):
            print("salida ", i)
            for j in range(len(entradas)):
                print("datos actuales:", entradas[j], self.pesos[j][i], self.umbrales[i])
                salida[i] += (entradas[j] * self.pesos[j][i]) 
                print("resultado: ", salida[i])
            salida[i] = salida[i] - self.umbrales[i]
        return salida
    
    def output_error(self):

        self.erroresSalida = [0] * self.numeroSalidas

        for i in range(self.numeroSalidas):
            self.erroresSalida[i] = self.salidaOriginal[i] - self.salidaSistema[i]

    def pattern_error(self):
        for valor in self.erroresSalida:
            errorPatron = errorPatron + abs(valor)
        errorPatron = errorPatron / (self.numeroSalidas)
        return errorPatron

    def update_weights(self, rataAprendizaje, entradas):
        for i in range(self.numeroSalidas):
            for j in range(len(self.patrones)):
                self.pesos[j][i] = self.pesos[j][i] + rataAprendizaje * self.erroresSalida[i] * self.entradas[j]

    def update_thresholds(self,rataAprendizaje):
        for i in range(self.numeroSalidas):
            self.umbrales[i] = self.umbrales[i] + rataAprendizaje * self.erroresSalida[i] * 1

    def error_checking(self, errorPermitido):
        if(self.sumatoriaErroresPatron <= errorPermitido):
            return True
        else:
            return False

    def analysis_of_all_patterns(self,funcionActivacion, rataAprendizaje, errorPermitido):
        matrizCorrectora = []
        for i in range(len(self.patrones)): 
            columna = [fila[i] for fila in self.patrones]
            columnaSalida = [fila2[i] for fila2 in self.salidaOriginal]
            matrizCorrectora.append(columnaSalida)
            self.salidaSistema.append(self.get_output(columna))
            self.output_error()
            sumatoriaErroresPatron = self.pattern_error() + sumatoriaErroresPatron
            self.update_weights(rataAprendizaje, columna)
            self.update_thresholds(rataAprendizaje)
        self.salidaOriginal=matrizCorrectora
        self.activation_funcion(funcionActivacion)
        return self.error_checking(errorPermitido)

    def patterns_according_to_interactions(self,funcionActivacion, rataAprendizaje, errorPermitido, numeroInteracciones):
        for i in range(numeroInteracciones):
            if (self.analysis_of_all_patterns(funcionActivacion,rataAprendizaje, errorPermitido) == True):
                return i
        return numeroInteracciones

    def file_upload(self,filename):

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
                self.patrones.append(filaEntradas)
            
            if(matriz[0][i] == 0):
                for j in range(1, filas):
                    b = matriz[j][i]
                    filaSalidas.append(b)
                self.salidaOriginal.append(filaSalidas)
        self.create_weights_thresholds()

    def activation_funcion(self,funcionActivacion):
        columnas = len(self.salidaSistema[0])
        filas = len(self.salidaSistema)
        if(funcionActivacion == "Perceptron"):
            for i in range(columnas):
                for j in range(1, filas):
                    if(self.salidaSistema[j][i] < 0):
                        self.salidaSistema[j][i] == 0
                    else:
                        self.salidaSistema[j][i] == 1

    def create_weights_thresholds(self):
        self.numeroEntradas = len(self.patrones)
        self.numeroSalidas = len(self.salidaOriginal)
        self.pesos = [[random.uniform(0, 1) for j in range(self.numeroSalidas)] for i in range(self.numeroEntradas)]
        self.umbrales = [random.uniform(0, 1) for j in range(self.numeroSalidas)]