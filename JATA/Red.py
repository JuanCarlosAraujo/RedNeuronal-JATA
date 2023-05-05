import random


def Red():
    YR=[0] * 3 
    X = [random.randint(0, 1) for _ in range(5)]
    print("Entradas: ", X)
    W=[[random.random() for j in range(3)] for i in range(5)]
    print("Pesos: ", W )
    U=[random.random() for _ in range(3)]
    print("Umbrales: ",U)
    EL=[0] * 3
    Yd=[random.randint(0, 1) for _ in range(3)]
    print("Salidas: ", Yd)
 
    #calcular valor de las salidas
    get_output(Yd, YR, X, W, U)
    print("Salidas Obtenidas: ", YR)

    #Calcular Error por patron
    output_error(EL,Yd,YR)
    print("Error por patron:", EL)

def get_output(Yd, YR, X, W, U):
    print("calculando salida...")
    for i in range(len(Yd)):
        print("salida ", i)
        for j in range(len(X)):
            print("datos actuales:", X[j], W[j][i], U[i])
            YR[i] += (X[j] * W[j][i]) - U[i]
            print("resultado: ", YR[i])

def output_error(EL,Yd,YR):
    for i in range(len(Yd)):
        EL[i] = Yd[i] - YR[i]


