def media_matriz(matriz):
    """A função recebe uma matriz (lista de listas) cujos elementos
    são números inteiros e retorna a média entre esses números
    com duas casas decimais de precisão (float)."""
    elementos = []
    for linha in matriz:
        for elemento in linha:
            elementos.append(elemento)
    return sum(elementos)/len(linha)*len(matriz)