def eh_quadrada(matriz):
    """Dada uma matriz, retorna se a mesma é ou não quadrada:
    list(list)-->bool"""
    linha_matriz=len(matriz)
    coluna_matriz=len(matriz[0])
    if linha_matriz!=coluna_matriz:
        return False
    else:
        return True