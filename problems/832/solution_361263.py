def eh_quadrada(matriz):
    """dado uma matriz retorna true se for
    quadrada e false se não for; list[list[float]]->bool"""
    if len(matriz)==len(matriz[0]):
        return True
    else:
        return False