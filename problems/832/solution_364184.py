def eh_quadrada (matriz):
    '''função que identifica se uma matriz é quadrada,retorna
    True se for e False se não;list->bool'''
    linha=(len(matriz))
    col=(len(matriz[0]))
    for i in matriz:
        if linha == col or linha ==0:
            return True
        else:
            return False