def eh_quadrada(M):
    '''dada uma matriz, identifica se a matriz é quadrada, retornando
    True caso seja, caso contrário retorna False;
    list->bool'''
    if len(M)==0 or len(M)==len(M[0]):
        return True
    else:
        return False