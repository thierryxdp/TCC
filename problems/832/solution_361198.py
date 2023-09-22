def eh_quadrada(m):
    '''fucao que indica se uma dada matriz de entrada é quadrada
    ou nao. 
    matriz -> bool'''
    if m == []:
        return True
    elif len(m) == len(m[0]):
        return True
    else:
        return False