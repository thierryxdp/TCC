def media_matriz(matriz):
    '''Recebe uma matriz em forma de lista
    e retorna a média dos elementos 
    existentes na lista
    list->float'''
    soma=0
    qtd_ele=0
    for i in matriz:
        for j in i:
            soma=soma+int(j)
            qtd_ele=qtd_ele+1
    return round(soma/qtd_ele,2)