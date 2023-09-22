'''
	Funçãoque dado um número inteiro e uma matriz 
    de inteiros de tamanho qualquer, conta e retorna quantas 
    vezes aquele número aparece na matriz.
    i:int
    j:int
    contador:int
    numero:int
    matriz:int
    return:int
'''
def conta_numero(numero ,matriz):
    contador = 0
    i = 0
    j = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[i]):
            if matriz[i][j] == numero:
                contador += 1
            j += 1
        i += 1
    return contador