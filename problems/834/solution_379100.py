def media_matriz(matriz:list)->float:
    '''retorna média da matriz'''
    soma=0
    total=0
    for i in matriz:
        for j in i:
            soma+=j
        total+=len(i)
    return round(soma/total,2)