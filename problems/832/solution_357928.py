def eh_quadrada(matriz):
    "Retorna se uma matriz é quadrada ou não. list->bool"
    for linha in matriz:
        for coluna in linha:
            if coluna != [] or linha != coluna:
                return False
    return True