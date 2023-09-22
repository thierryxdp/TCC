def eh_quadrada(matriz):
    "Retorna se uma matriz é quadrado ou não. list->bool"
    for linha in matriz:
        for coluna in linha:
            if coluna != []:
                return False
    return True