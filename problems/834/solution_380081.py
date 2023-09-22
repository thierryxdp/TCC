def media_matriz(matriz):
    '''funçao que dada uma matriz retorna a media de todos
os numeros da matriz.
list -> float'''
    quant_num=len(matriz)*len(matriz[0])
    lista=[]
    for linha in matriz:
        for coluna in linha:
            lista.append(coluna)
    soma_matriz= sum(lista)
    media= soma_matriz/quant_num
    return round(media,2)