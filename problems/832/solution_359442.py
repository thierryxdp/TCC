def eh_quadrada(matriz: list):
    primeira_linha = matriz[0]
    
    for i in matriz:
        if not len(i) == len(matriz[0]):
            return False
        else:
            return True