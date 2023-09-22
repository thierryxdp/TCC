def media_matriz(matriz):
    '''Dada uma matriz de números inteiros não vazia, retorna
    a média de todos os números da matriz (com duas casas
    decimais de precisão).
    list -> float'''
    lista=[]
    numerador=sum(lista)
    denominador=len(lista)
    media=numerador/denominador
    media_arredondada=round(media,2)
    for i in matriz:
        lista=lista+matriz[i]
    return media_arredondada