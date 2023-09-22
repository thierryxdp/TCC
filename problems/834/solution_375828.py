def media_matriz(matriz):
    '''retorna a media de todos os numeros da matriz
    matriz -> float'''
    soma = 0
    termos = 0
    for L in range(len(matriz)):
        for c in range(len(matriz[L])):
            soma = soma + matriz[L][c]
            termos += 1
        media = soma/termos
    return round(media,2)