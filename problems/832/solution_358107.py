def eh_quadrada(matriz):
    '''função que identifica se uma matriz é quadrada. lista->bool'''
    if matriz==[]:
        return True
    l=len(matriz)
    c=len(matriz[0])
    if l==c:
        return True
    else:
        return False