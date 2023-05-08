import random


def Red():
    errorPatron = 0
    rataAprendizaje = 0,1
    salidaSistema=[0] * 3 
    entradas = [random.randint(0, 1) for _ in range(5)]
    print("Entradas: ", entradas)
    pesos=[[random.random() for j in range(3)] for i in range(5)]
    print("Pesos: ", pesos )
    umbrales=[random.random() for _ in range(3)]
    print("Umbrales: ",umbrales)
    erroresSalida=[0] * 3
    salidaOriginal=[random.randint(0, 1) for _ in range(3)]
    print("Salidas: ", salidaOriginal)
 
    #calcular valor de las salidas
    get_output(salidaOriginal, salidaSistema, entradas, pesos, umbrales)
    print("Salidas Obtenidas: ", salidaSistema)

    #Calcular Error por salida
    output_error(erroresSalida,salidaOriginal,salidaSistema)
    print("Error por patron:", erroresSalida)

    #Calcular el error por patron
    pattern_error(erroresSalida, salidaOriginal, errorPatron)
    print(errorPatron)

    #Actualizar pesos
    update_weights(pesos, salidaOriginal, entradas, rataAprendizaje, erroresSalida)

    #Actualizar umbrales
    update_thresholds(umbrales, salidaOriginal, rataAprendizaje, erroresSalida)

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
    errorPatron = sum(abs(x) for x in erroresSalida) / salidaOriginal

def update_weights(pesos, salidaOriginal, entradas, rataAprendizaje, erroresSalida):
    for i in range(len(salidaOriginal)):
        for j in range(len(entradas)):
            pesos[j][i] = pesos[j][i] + rataAprendizaje * erroresSalida[i] * entradas[j]

def update_thresholds(umbrales, salidaOriginal, rataAprendizaje, erroresSalida):
    for i in range(len(salidaOriginal)):
        umbrales[i] = umbrales[i] + rataAprendizaje * erroresSalida[i] * 1




