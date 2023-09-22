def media_matriz(matriz):
    """A função recebe como entrada uma matriz de inteiros
    não vazia, e deve retornar a média de todos os números
    da matriz com duas casas decimais de precisão
    Entrada: List
    Saída: Float"""
    
    posicao=0
    valor=0
    media=valor/2
    for i in range(len(matriz)):
        valor += matriz[posicao]
    return media