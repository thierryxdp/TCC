def conta_numero(numero,matriz):
    '''recebe um número inteiro e uma matriz e retorna 
    quantas vezes esse número aparece na matriz
    int,int[int]->int'''
    count = 0
    for i in len(matriz):
        count = count + list.count(matriz[i],numero)
    return count