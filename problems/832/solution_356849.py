def eh_quadrada(n):
    """essa função verifica se uma matriz é quadrada comparando as linhas e colunas
    lista-->bolean"""
    if n == []:
        return True
    else:
        return len(n)==len(n[0])