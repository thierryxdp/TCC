def conta_numero(numero, matriz):
    '''dado um numero inteiro e uma matriz de inteiros de tamanho qqr, conta e
retorna qts vezes aquele numero aparece na matriz'''
    #list, int > int
    for numero in matriz:
        cont = matriz.count(numero)
        return cont