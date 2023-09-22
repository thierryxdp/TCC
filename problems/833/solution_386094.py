def conta_numero(n:int,matriz:list)->int:
    '''quantas vezes o número n aparece na matriz'''
    contador=0
    for i in matriz:
        contador+=i.count(n)
    return contador