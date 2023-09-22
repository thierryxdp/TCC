def eh_quadrada(matriz: list):
    primeira_linha = matriz[0]
    
    if len(matriz) == 0:
        return True
    
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False