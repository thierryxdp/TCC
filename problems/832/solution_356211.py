def eh_quadrada (matriz):
    """Função que identifica se a matriz fornecida é quadrada. Retorna True
    em caso positivo e False em caso negativo."""
    """list-->bool"""
    if len(matriz)==0:
        return True
    for j in matriz:
        if len(j)==len(matriz):
            return True
        else:
            return False