import math
def eh_quadrada(matriz):
    somatorio=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
        	somatorio=matriz[i][j]+somatorio
    return somatorio