def eh_quadrada(m):
    qtd_linhas=len(m)
   
 
    for i in range(qtd_linhas):
        for j in range(qtd_colunas):
            if i==j :
                a=True
            elif i!=j:
                a=False
            
    return  a