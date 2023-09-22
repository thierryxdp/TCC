def media_matriz(matriz):
    '''Dada uma matriz nao vazia 
retorna a media de todos seus numero.
list->float.'''
    lin = len(matriz)
    col =len(matriz[0])
    soma = 0
    acumulador =0
    for i in range (0,lin):
        for c in range (0,col):
            soma = soma + matriz[i][c] 
            acumulador =+1
    return soma / acumulador