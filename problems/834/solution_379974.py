def media_matriz(matriz):
    """A função recebe uma matriz (lista de listas) cujos elementos
    são números inteiros e retorna a média entre esses números
    com duas casas decimais de precisão (float)."""
    for linha in matriz:
        for elementos in linha:
            return sum(elementos)/(len(linha)*len(matriz))