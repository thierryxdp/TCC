def eh_quadrada(matriz):
    '''função que recebe uma matriz, em lista, como entrada e retorna o valor
booleano "True" caso a matriz seja quadrada, e "False" caso não seja;
list(list)->bool'''

    if len(matriz)==0 or len(matriz[0])==0:
        return True

    nlin=len(matriz)
    ncol=len(matriz[0])

    if nlin == ncol:
        return True

    else:
        return False