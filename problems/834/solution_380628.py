def media_matriz(matriz):
    soma_total=0
    total_elem=len(matriz)*len(matriz[0])
    for linha in matriz:
        soma_linha=0
        for elem in linha:
            soma_linha+=elem
        soma_total+=soma_linha
    media=soma_total/total_elem
    return round(media,2)