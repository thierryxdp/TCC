def eh_quadrada(x):
    if x == []:
        return False
    nlinha = len(x)
    ncoluna = len(x[0])
    if nlinha == ncoluna:
        return True
    else:
        return False