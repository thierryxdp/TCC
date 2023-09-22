def eh_quadrada(x):
    if x == []:
        return True
    nlinha = len(x)
    ncoluna = len(x[0])
    if nlinha == ncoluna:
        return True
    else:
        return False