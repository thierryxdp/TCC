def eh_quadrada(m):
    '''  funaco qur recebe uma matiz e retorna true se for matiz quadada ou []
    e false se nao for quadrada; lista(matriz)-> bool'''
    if m==[]:
            return True
    qtd_linhas=len(m)
    qtd_colunas=len(m[0])
    
    for i in range(qtd_linhas):
        for j in range(qtd_colunas):
            if i==j:
                a=True
            else:
                a=False
    return a