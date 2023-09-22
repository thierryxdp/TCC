def eh_quadrada(mat):
    """A função que verifica se uma matriz é quadrada
    matriz --> boolean"""
    if(len(mat)==len(mat[0]) or mat==[]):
        return 0==0
    else:
        return 0!=0