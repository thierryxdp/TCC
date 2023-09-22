def eh_quadrada(m):
    '''  funaco que recebe uma matiz quadrada e retorna um booleano
    ; list-> bool'''
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