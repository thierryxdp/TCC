def eh_quadrada(matriz: list):
    primeira_linha = matriz[0]
    
    if len(matriz) < 2:
        return False
    if len(matriz) == 0:
        return True
    
    for i in matriz: 
        if len(i) == len(matriz[0]):
            return False