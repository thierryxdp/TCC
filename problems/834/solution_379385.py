def media_matriz(m):
    '''Função que retorna a média de todos os números da matriz, com duas casas de precisão. list-> float'''
    i=0
    a=0
    d=0
    for s in m:
    	a+=sum(m[i])
    	d+=len(m[i])
        i=i+1
    return round(a/d,2)