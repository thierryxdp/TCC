def media_matriz(matriz):
    """Função que dada uma matriz de inteiros não vazia,retorna a média
dos números da matriz; list->float"""
    lista=[]
    for elemento in matriz:
        for numero in elemento:
            lista.append(numero)
    media=(sum(lista))/(len(lista))
    return round(media,2)