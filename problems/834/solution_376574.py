def media_matriz(matriz):

    qtd_elementos=len(matriz)*len(matriz[0])
    soma_elementos=0

    for linha in matriz:
        for j in linha:
            soma_elementos+=j

    media=soma_elementos/qtd_elementos

    return round(media,2)