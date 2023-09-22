def eh_quadrada(matriz):
    ""
    i = []
    for linha in matriz:
        for coluna in linha:
            if coluna and linha  != i:
                return False
    return True