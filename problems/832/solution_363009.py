def eh_quadrada(mat):
    """funcao que retorna true se uma matriz for quadrada e false se nao for; list->bool"""
    if len(mat)>0:
        if len(mat)==len(mat[0]):
            return True 
        else:
            return False
    else:
        return True