def eh_quadrada(matriz):
    ""
    cont = 0
    for linha in matriz:
        for coluna in linha:
            if coluna != []:
                cont += 1
                return False
    return True