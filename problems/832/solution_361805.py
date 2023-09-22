def eh_quadrada(matriz):
    ''''''
    
    for linha in matriz:
        if len(linha)!=len(matriz):
            return False
        if len(linha)==len(matriz):
            return True
        if linha[0]:
            return True