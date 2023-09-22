def media_matriz(m):
    '''função que calcula a média dos valores da matriz
    	list --> float'''
    soma = 0
    nlin = len(m)
    if nlin > 0:
    	ncol = len(m[0])
    for linha in m:
        for valor in linha:
            soma = soma + valor
    		media = soma/(nlin*ncol)
    return round(media, 2)