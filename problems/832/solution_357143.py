def eh_quadrada(matriz):
    """funcao que identifica se uma matriz e quadrada.
    lista->bool"""
    m=len(matriz)
    n=len(matriz[0])
    if matriz==[[]]:
        return "True"
    if m==n:
        return "True"
    else:
        return "False"