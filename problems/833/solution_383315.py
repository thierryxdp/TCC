def conta_numero(numero, matriz):
    '''Funcao que dado um numero inteiro e uma matriz de inteiros de tamanho qualquer,
    conta e retorna quantas vezes aquele numero aparece.
    list -> int'''
    
    conta = 0
    
    for i in range(len(matriz)):
        conta += list.count(matriz[i], numero)
    
    return conta