def eh_quadrada(matriz):
    ''''''
    linha = matriz[0]
    coluna = matriz[0][0]
    
    
    if linha in matriz:
        return False
    if matriz not in linha and coluna:
        return True