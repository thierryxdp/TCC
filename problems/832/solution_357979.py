def eh_quadrada(matriz):
    quantidadeElementos = len(matriz)
    for linha in matriz:
        if len(linha) != quantidadeElementos:
            return False
        
    return True