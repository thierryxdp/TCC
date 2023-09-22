def eh_quadrada (matriz):
    """Retorna True se uma dada matriz for quadrada e False no caso contrário.
    Entrada, list(list)
    Saida: bool"""
    if len(matriz)>0:
        if len(matriz) == len(matriz[0]):
            return True
        else:
            return False
        else:
            return True