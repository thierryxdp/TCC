def conta_numero(numero, matriz):
    '''Função retorna, dada um numero inteiro e uma matriz de tamanho qualquer,
    quantas vezes esse determinado numero aparece na lista'''
    indice = 0
    resultado = 0
    tamanho = len(matriz)
    while indice < tamanho:
        resultado+= matriz[indice].count(numero)
        indice+= 1
    return resultado