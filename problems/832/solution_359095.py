def eh_quadrada(mat):
    '''funcao que identifica se uma matriz é quadrada;
    list->bool'''
    if len(mat)==0:
        return True
    f=0
    g=len(mat)
    h=range(g)
    while f in h:
        if len(mat[f])==g:
            f=f+1
    return True 
    
    if len(mat)!=len(mat[0]):
        return False