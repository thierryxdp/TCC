def media_matriz(matriz):
    '''funcao que dada uma matriz de numeros inteiros e nao vazia, retorna a media de todos os numeros dessa matriz com no maximo 2 casa decimais;
        list(list)-> float'''
    media= 0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            media= matriz[linha][coluna]+media
    return round(media/(len(matriz)*len(matriz[0])),2)