def eh_quadrada(matriz):
    ""
 
    for linha in matriz:
        for coluna in linha:
            if coluna == []:
                return True
    return False