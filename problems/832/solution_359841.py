def eh_quadrada (matriz):
    """Função que retorna se a matriz enviada é ou não quadrada
    list -> bool"""
    if not matriz:
        return True
    i = len(matriz)
    j = len(matriz[0])
    if i == j:
        return True
    else:
        return False