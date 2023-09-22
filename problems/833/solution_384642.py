def conta_numero(numero, matriz):
    '''Função retorna, dada um numero inteiro e uma matriz de tamanho qualquer,
    quantas vezes esse determinado numero aparece na lista'''
    tamanho = len(matriz)
    resultado = 0
    indice = 0 
    while indice < tamanho:
        resultado+= matriz[indice].count(numero)
        indice+= 1
        
    return resultado