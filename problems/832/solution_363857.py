def eh_quadrada (matriz):
    '''função que identifica se uma matriz é quadrada,retorna
    True se for e False se não;list->bool'''
    for i in matriz:
        linha=(len(matriz))
        col=(len(matriz[0]))
        if linha == col or col==0:
            return True
        else:
            return False