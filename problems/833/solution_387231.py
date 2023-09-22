def conta_numero(numero,matriz):
    '''funcao que recebe um numero e uma matriz e retorna 
       o numero de vezes que esse numero apareceu na matriz.
       int, list(list) -> int'''
    i= 0
    for x in range(len(matriz)):
        for y in range(len(matriz[0])):
            if matriz[x][y] == numero:
                i+= 1
    return i