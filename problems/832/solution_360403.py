def eh_quadrada(m):
    '''Retorna 'True', se a matriz m de entrada for  quadrada;
       'False', caso contrário;
       list -> bool'''
    if len(m)==len(m[0]) or len(m)==0:
        return True
    return False