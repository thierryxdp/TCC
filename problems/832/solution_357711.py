def eh_quadrada(matriz):
    """Função na qual dada uma matriz, verifica se ela é quadrada ou não."""
    if len(matriz)== len(matriz[0]):
        return True
    elif matriz == []:
        return True
    else:
        return False