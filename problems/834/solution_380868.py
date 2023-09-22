def media_matriz(matriz):
    '''essa funçao retorna a media de todos os numeros de uma matriz nao vazia, com a precisao
    de duas casas decimais
    list -> float'''
    lista= [] 
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            list.append(lista, matriz[i][j])
    media=sum(lista)/len(lista)
    return round(media,2)