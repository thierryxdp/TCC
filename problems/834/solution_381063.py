def media_matriz(matriz):
    '''Função que dada uma matriz retornará a média da soma de todos os termos da matriz
    matrix -> float'''

    soma = 0
    i = 0
    quantidade = 0 
    
    if len(matriz) != 0:
        while i < len(matriz):
            soma += sum(matriz[i])
            quantidade += len(matriz[i])
            i += 1
    media = soma/quantidade
    return round(media,2)