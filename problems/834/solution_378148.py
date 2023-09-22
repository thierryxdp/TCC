def media_matriz(matriz):
    cont_elementos = 0
    media = 0
    for linha in matriz:
        for elemento in linha:
            media += elemento
            cont_elementos += 1
	media /= cont_elementos
    return round(media,2)