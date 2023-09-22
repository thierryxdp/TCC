def eh_quadrada(m):
    qtd_linhas=len(m)
    qtd_colunas=len(m[0])
    a=[]
    for i in range(qtd_linhas):
        for j in range(qtd_colunas):
            if i==j :
                a=True
            elif i!=j:
                a=False
            else:
                a=True 
    return  a