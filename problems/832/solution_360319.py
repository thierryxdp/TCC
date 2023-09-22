def eh_quadrada (matriz):
    """dada uma matriz, identifica se ela é quadrada;
    lista->bool."""
    if matriz==[]:
        return True
    if len(matriz)==len(matriz[0]):
        return True
    else:
        return False