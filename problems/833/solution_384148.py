def conta_numero(numero, matriz):
    """função que dado um número inteiro e uma matriz de números inteiros, retorna quantas vezes o número aparece na matriz;int,list-->int"""
    vezes=0
    for i in range(len(matriz)):
            if i in matriz:
                vezes+=i.count(numero)
    return vezes