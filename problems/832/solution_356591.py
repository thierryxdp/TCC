def eh_quadrada(x):
    """essa função verifica se uma matriz é quadrada comparando as linhas e colunas
    lista-->bolean"""
    if x == []:
        return True
    else:
        return len(x)==len(x[0])