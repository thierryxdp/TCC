def media_matriz(matriz):
    '''Dada uma matriz inteira não vazia,
    retorna a media de todos os numeros dessa matriz
    list -> float'''
    
    soma=0
    n_elementos=0
    linha=len(matriz)
    col=len(matriz[0])
    for i in range(linha):
        for j in range(col):
            soma+=matriz[i][j]
            n_elementos+=1
    media=soma/n_elementos
    return round(media,2)