def eh_quadrada(m):
    '''Função retorna se uma matriz é quadrada ou não
       list-->bool'''
    if len(m)>0 and len(m)==len(m[0]):
        return True
    elif m==[]:
        return True
    else:
        return False