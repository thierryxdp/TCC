def eh_quadrada(matriz):
    "Retorna se uma matriz é quadrada ou não. list->bool"
    for linha in matriz:
        for coluna in linha:
            if coluna == []:
                return True
    return False