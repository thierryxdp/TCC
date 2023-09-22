def eh_quadrada(matriz):
    matriz = []
    linha = len(matriz)
    coluna = len(matriz[0])
    
    for linha in range(matriz):
        for coluna in range(matriz):
            if len(matriz) == len(matriz[linha]) and len(matriz[coluna]):
                return True
            else:
                return False
    return True