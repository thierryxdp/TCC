def media_matriz(matriz):
    '''
       funcao que dada uma matriz de
       inteiros não vazia, retorna a media de
       todos os numeros da matriz
    '''
    media=0
    a=len(matriz)
    b=len(matriz[0])
    for n in matriz:
        for e in n:
            media=media+e
            conta=media/(a*b)
    return round(conta,2)