def media_matriz(matriz):
    """A função recebe como entrada uma matriz de inteiros
    não vazia, e deve retornar a média de todos os números
    da matriz com duas casas decimais de precisão
    Entrada: List
    Saída: Float"""
    
    valor=0
    media=valor/2
    posicao=0
    numero=matriz[posicao]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            valor+= matriz[posicao]
    posicao+= 1
    return round(media,2)