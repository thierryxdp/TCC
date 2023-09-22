def conta_numero(numero, matriz):
    '''Função retorna, dada um numero inteiro e uma matriz de tamanho qualquer,
    quantas vezes esse determinado numero aparece na lista'''
    indice = 0
    resultado = 0
    tamanho = len(matriz)
    while x < tamanho:
        resultado+= matriz[x].count(numero)
        indice+= 1
    return resultado