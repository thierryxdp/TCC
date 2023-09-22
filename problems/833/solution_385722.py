def conta_numero(numero,matriz):
    """ Dado um número inteiro e uma matriz de inteiros de tamanho qualquer, conta e retorna quantas vezes aquele número aparece na matriz"""
    l=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            l=l+[matriz[i][j]]
    return l.count(numero)