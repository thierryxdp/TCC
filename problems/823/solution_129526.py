def faltante(lista):
    '''faltante recebe uma list e devolve um numero
    inteiro que esta faltando na lista
    determina o numero que esta faltando numa determinada lista
    list --> int'''
    
    posicao = 1
    
    lista.sort()
    while posicao in lista:
        posicao+=1
    return posicao