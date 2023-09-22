def eh_quadrada(m):
    '''
    	essa função recebe uma matriz e identifica se ela é quadrada, ou seja,
        possui o mesmo num de linha e colunas
        list->bool
    '''
    if len(m)!= len(m[0]) or m = []:
        return False
    else:
        return True