def media_matriz(matriz):
    '''retorna a média da matriz.
    	matriz --> float'''
    cont = 0
    soma = 0
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            cont = cont +1
            soma = soma + matriz[x][y]
    media = soma / cont
    return round(media,2)