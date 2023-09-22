def eh_quadrada (matriz):
    """Recebe uma matriz, testa se ela possui o mesmo número
    de linhas e colunas, e retorna um valor booleano se isso
    for verdade.
    list -> bool"""
    linha = len(matriz)
    coluna = len(matriz[0])
    if linha == coluna:
                 return True
    else:
                 return False