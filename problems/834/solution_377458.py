def media_matriz(matriz):
    lista = []
    for i in matriz:
        lista += i[::]
    media = round(sum(lista)/len(lista),2)
    return media