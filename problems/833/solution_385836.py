def conta_numero(numero, matriz):
    """dada um número inteiro e uma matriz de inteiros de tamanho qualquer, a função
    retorna a quantidade de vezes que o número aparece na matriz;
    int,list(list)->int"""
    linha=len(matriz)
    contador=0
    for i in range(linha):
        contador= contador+ list.count(matriz[i],numero)
    return contador