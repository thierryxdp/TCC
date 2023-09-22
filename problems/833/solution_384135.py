def conta_numero(numero, matriz):
    """função que dado um número inteiro e uma matriz de números inteiros, retorna quantas vezes o número aparece na matriz;int,list-->int"""
    x=0
    y=0
    vezes=0
    for i in range(len(matriz)):
        if numero in matriz:
            vezes=vezes+matriz.count(numero)
    return sum.(vezes)