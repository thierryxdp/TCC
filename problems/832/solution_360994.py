def eh_quadrada(m):
    """Função que, dado uma matriz, retorna se ela é ou não quadrada
    list-->bool"""
    linhas = len(m)
    colunas = int
    if m == []:
        return True
    for i in range(linhas):
        colunas = len(m[0])
        if linhas == colunas:
            return True
    if linhas != colunas:
        return False