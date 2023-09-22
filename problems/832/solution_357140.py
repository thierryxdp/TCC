def eh_quadrada(matriz):
    """funcao que identifica se uma matriz e quadrada.
    lista->bool"""
    m=len(matriz)
    n=len(matriz[0])
    if m==n:
        return "True"
    else:
        return "False"