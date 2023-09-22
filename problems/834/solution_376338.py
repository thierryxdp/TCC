def media_matriz(m):
    """Dado uma matriz como entrada, retorna a media dos elementos desta
    matriz com exatamente duas casas decimais;
    list(list(int))->float"""
    aij=[]
    linhas=len(m)
    colunas=len(m[0])
    for i in range(linhas):
        for j in range(colunas):
            aij.append(m[i][j])
    return round(sum(aij)/(len(aij)),2)