def eh_quadrada(m):
    # se a matriz é vazia
    if len(m) == 0:
        return True
    
    qtd_linhas = len(m)
    qtd_colunas = len(m[0])
    
    return qtd_linhas == qtd_colunas