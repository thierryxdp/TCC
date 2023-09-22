def filtra_pares(x1,x2,x3,x4):
    #"Função que recebe uma tupla e retorna uma tupla quando as entras forem divisíveis por 2"
    '''int, int, int ,int--->tupla'''
    if x1%2==0 and x2%2==0 and x3%2==0 and x4%2==0:
        return x1 , x2 , x3 , x4
    elif x1%2==0 and x2%2==0 and x3%2==0:
        return x1 , x2 , x3
    elif x1%2==0 and x2%2==0 and x4%2==0:
        return x1 , x2 , x4
    elif x1%2==0 and x3%2==0 and x4%2==0:
        return x1 , x3 , x4
    elif x2%2==0 and x3%2==0 and x4%2==0:
        return x2 , x3 , x4
    elif x1%2==0 and x2%2==0:
        return x1 , x2
    elif x1%2==0 and x3%2==0:
        return x1 , x3
    elif x1%2==0 and x4%2==0:
        return x1 , x4
    elif x2%2==0 and x3%2==0:
        return x2 , x3
    elif x2%2==0 and x4%2==0:
        return x2 , x4
    elif x3%2==0 and x4%2==0:
        return x3 , x4
    elif x1%2==0:
        return x1
    elif x2%2==0:
        return x2
    elif x3%2==0:
        return x3
    elif x4%2==0:
        return x4