def eh_quadrada(m):
    b=[]
    qtd_colunas=len(m[0])
    qtd_linhas=len(m)
    
    for i in range(qtd_linhas):
        for j  in range(qtd_colunas):
            if i==j:
                a=True
            elif i!=j:
                a=False
            else:
                a=True
            
    return  a