def conta_numero(numero, matriz):
    '''dado um numero inteiro e uma matriz de inteiros de tamanho qualquer, calcula e retorna quantas vezes aquele numero aparece na matriz'''
    '''int,list->int'''
    qt=0
    for numeros in len(matriz[0]):
        if numeros == numero:
            qt+=1
    return qt