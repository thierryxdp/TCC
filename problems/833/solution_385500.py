def conta_numero(numero, matriz):
    '''dado um numero inteiro e uma matriz de inteiros de tamanho qualquer, calcula e retorna quantas vezes aquele numero aparece na matriz'''
    '''int,list->int'''
    qt=0
    i=0
    for numeros in matriz[0][i]:
        if numeros == numero:
            qt+=1
    return qt