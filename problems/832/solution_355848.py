def eh_quadrada(m):
    '''Dada uma matriz, a função retorna se a mesma é quadrada ou não
       list -> bool
       Parametros:
       m: matriz a ser digitada'''
    if len(m) == len(m[0]):
        return True
    else:
        return False