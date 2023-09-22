def eh_quadrada(m):
    '''Retorna um booleano identificando se a matriz m é quadrada. Obs:matrizes vazias são quadradas.
    list(list)->bool'''
    if len(m)!=0:
        return len(m)==len(m[0])
    else:
        return True