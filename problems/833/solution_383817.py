def conta_numero(numero,matriz):
    '''Dado um numero inteiro e uma matriz de inteiros de tamanho qualquer, 
    conta e retorna qunatas vezes aquele numero aparece na matriz.
    int, list -> int'''
    vezes=0
    i=0
    while i<len(matriz):
        vezes= vezes + list.count(matriz[i],numero)
    	i=i+1
    return vezes