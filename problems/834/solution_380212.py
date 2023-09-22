def media_matriz(matriz):
    """dada uma lista matriz de inteiros não vazia,
    retorna a média aritmética de todos os numeros da matriz
    list --> float"""
    lista_media=[]
    for linha in matriz:
        for coluna in linha:
            lista_media=lista_media+[coluna]
    media=sum(lista_media)/len(lista_media)
    return round(media,2)