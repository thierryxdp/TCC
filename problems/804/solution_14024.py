def filtra_pares(x1,x2,x3,x4):
    #"Função que recebe uma tupla e retorna uma tupla quando as entras forem divisíveis por 2"
    '''int, int, int ,int--->tupla'''
    tuplas= [x1,x2,x3,x4]
    tupla= tuplas[x1%2==0 , x2%2==0 , x3%2==0 , x4%2==0]
    return x1 , x2 , x3 , x4