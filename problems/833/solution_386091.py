def conta_numero(matriz:list,n:int)->int:
    '''quantas vezes o número n aparece na matriz'''
    contador=0
    for i in matriz:
        contador+=i.count(n)
    return contador