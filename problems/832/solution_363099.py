def eh_quadrada(m):
    '''Retorna 'True' se a matriz dada é quadrada;
    list -> boolean'''
    
    if m == []:
        return True
    else:
        for i in range(len(m)):
            if len(m) != len(m[i]):
                return False
            else:
                return True