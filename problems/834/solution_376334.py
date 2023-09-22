def media_matriz(m):
    """coment"""
    aij=[]
    for i in m:
        for j in m:
            aij.append(m[i][j])
    round(sum(aij)/(len(aij)),2)