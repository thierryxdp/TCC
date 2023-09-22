def media_matriz(matriz):
    '''retorna a média da matriz.
    	matriz --> float'''
    cont = 0
    soma = 0
    for x in matriz:
        for y in matriz:
            cont = cont +1
            soma = soma + matriz [x][y]
    media = soma / cont
    return media