def eh_quadrada(m):
    ''' função que retorna se uma matriz é quadrada, dada uma matriz (incluindo matrizes vazias)
    list --> bool'''
    numerolinhas = len(m)
    if len(m) == 0:
        return True 
    else:
        numerocolunas = len(m[0])
        if numerocolunas == numerolinhas:
            return True
        else:
            return False