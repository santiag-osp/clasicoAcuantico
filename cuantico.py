import numpy as np
import matplotlib.pyplot as plt


def canicas(M,V, clicks):
    index = 0
    vector = V
    while index < clicks:
        resp = M.dot(vector)
        vector = resp
        index += 1
    return vector

def probabilistico(clicks, rendijas, objetivos, arreglopos):
    dimension = 1 + rendijas + objetivos
    matriz = [[0 for i in range(dimension)] for j in range(dimension)]
    pro1 = 1/rendijas
    pro2 = rendijas/objetivos
    for i in range(rendijas):
        matriz[i+1][0] = pro1
    for i in range(rendijas +1, dimension):
        for j in range(dimension):
            if i == j:
                matriz[i][j] = 1
    x = rendijas + 1
    y = rendijas + arreglopos[0]
    for i in range(rendijas):
        for j in range(x, y+1):
            matriz[j][i+1] = pro2
        aux = y
        x = aux
        y += arreglopos[i]
    var = [0 for i in range(dimension)]
    var[0] = 1
    var1 = np.array(var)
    valor = np.array(matriz)
    index = 0
    while index < clicks:
        maxt = valor * valor
        vector = maxt
        index += 1
    return vector.dot(var1)


def probabilisticoC(clicks, rendijas, objetivos, arreglopos, probb1, probb2):
    dimension = 1 + rendijas + objetivos
    matriz = [[0 for i in range(dimension)] for j in range(dimension)]
    pro1 = probb1
    pro2 = probb2
    for i in range(rendijas):
        matriz[i+1][0] = pro1
    for i in range(rendijas +1, dimension):
        for j in range(dimension):
            if i == j:
                matriz[i][j] = 1
    x = rendijas + 1
    y = rendijas + arreglopos[0]
    for i in range(rendijas):
        for j in range(x, y+1):
            matriz[j][i+1] = pro2
        aux = y
        x = aux
        y += arreglopos[i]
    var = [0 for i in range(dimension)]
    var[0] = 1
    var1 = np.array(var)
    valor = np.array(matriz)
    index = 0
    while index < clicks:
        maxt = valor * valor
        vector = maxt
        index += 1
    return vector.dot(var1)



def graf(vector):
    grafica = [x for x in range(len(vector))]
    plt.bar(grafica, vector)
    plt.show()

def main():
    #test 1
    a = np.array([[0, 1 / 3, 2 / 3], [1 / 6, 1 / 2, 1 / 3], [5 / 6, 1 / 6, 0]])
    b = np.array([1/3, 0, 2/3])
    print(canicas(a, b, 1))
    #test 2
    # aqui podemos de una los valores 1 es el # de clicks
    # 2 es el # de rendijas,  6 el # de objetivos
    #y el arreglo cuantos objetivos tiene cada rendija
    print(probabilistico(1, 2, 6, [3, 3, 9]))
    #test 3
    # aqui podemos de una los valores 1 es el # de clicks
    # 4 es el # de rendijas,  8 el # de objetivos
    # y el arreglo cuantos objetivos tiene cada rendija, y los demas son las probabilidades
    print(probabilisticoC(1, 4, 8, [2, 2, 2, 2, 13], 1 / 4, 3 / 35))
    #test 4
    graf(canicas(a, b, 1))

main()