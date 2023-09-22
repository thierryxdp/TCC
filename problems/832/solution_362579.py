def eh_quadrada(mat):
    null=[]
    l=len(mat)
    c=len(mat[0])    
    for i in range(l):
        if mat[i] == null:
            return True
    if l == c:
        return True
    else:
        return False