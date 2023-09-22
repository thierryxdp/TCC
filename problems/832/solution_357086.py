def eh_quadrada(matriz):
    linha = len(matriz)
    for linha in matriz:
        if len(linha) != linha:
            return False
    return True