def media_matriz(matriz):
    '''retorna a media de todos os numeros da matriz
    matriz -> float'''
    contador = 0
    termos = 0
    for L in range(len(matriz)):
        for c in len(matriz[L]):
            contador = contador + L
            termos += 1
        media = contador/termos
    return round(media,2)