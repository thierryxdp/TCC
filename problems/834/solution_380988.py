def media_matriz(matriz):
    """ Função que recebe uma matriz com numeros inteiros e retorna a media dos números dessa matriz """
    listaElementos = []
    for linha in matriz:
        for e in linha:
            list.append(listaElementos, e)
    media = sum(listaElementos)/len(listaElementos)
    return round(media, 2)