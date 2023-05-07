import random


def Red():
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

    #Calcular Error por patron
    output_error(erroresSalida,salidaOriginal,salidaSistema)
    print("Error por patron:", erroresSalida)

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


