import math
def eh_quadrada(matriz):
    resultado=''
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
        	if matriz[i] == matriz[j]:
                resultado=True
    return resultado