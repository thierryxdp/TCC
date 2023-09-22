def media_matriz(matriz):
    """Função que dada a matriz da entrada retorna a media de todos os numeros da matriz; int-> float"""
    lista=[]
    for numero in matriz:
        lista=lista+numero
        media= lista/ len(matriz)
    return media