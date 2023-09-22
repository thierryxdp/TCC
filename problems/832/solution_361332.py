def eh_quadrada(mat):
    """identifica se a matriz dada é quadrada.
    list (of lists) -> bool"""
    a=len(mat)
    b=len(mat[0])
    if a==b or a==0 or b==0:
        return True
    else:
        return False