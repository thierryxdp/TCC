def conta_numero(numero, matriz):
    '''
    int,list ---- > int
    retorna quantas vezes numero passado aparece na matriz passada
    '''
    i = 0
    for linha in range(len(matriz)):
        i+=matriz[linha].count(numero)
    return i