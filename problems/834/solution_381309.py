def media_matriz(matriz):
    '''calcula a média de todos os
    números de uma matriz
    list --> float '''
    vol = 0
    cont = 0
    for a in matriz:
        cont += len(a)
        for b in a:
            vol += b
    return round(vol/cont,2)