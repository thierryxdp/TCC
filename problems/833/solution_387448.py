def conta_numero(numero, matriz):
    '''função que recebe uma matriz e um número e retorna quantas vezes o número aparece
    na matriz.
    float, list -> int'''
    contador = 0
    for x in range(len(matriz)):
        for z in range(len(matriz[x])):
        	if matriz[x][z] == numero:
            	contador = contador + 1
    return contador