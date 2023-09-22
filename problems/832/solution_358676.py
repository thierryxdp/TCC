def eh_quadrada(matriz):
    # caso especial de matriz "vazia"
    if len(matriz) == 1 and len(matriz[0]) == 0:
        return True
    # todas as linhas devem ter o mesmo tamanho da matriz 
    return all(len(matriz) == len(linha) for linha in matriz)