def eh_quadrada(mat):
    """identifica se a matriz dada é quadrada.
    list (of lists) -> bool"""
    a=len(mat)
    if a==0:
        return False
    b=len(mat[0])
    if a==b or b==0:
        return True
    else:
        return False