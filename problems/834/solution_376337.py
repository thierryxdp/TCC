def media_matriz(m):
    """coment"""
    aij=[]
    linhas=len(m)
    colunas=len(m[0])
    for i in range(linhas):
        for j in range(colunas):
            aij.append(m[i][j])
    return round(sum(aij)/(len(aij)),2)