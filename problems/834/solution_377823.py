def media_matriz(matriz):
    '''retorna a media dos numeros da matriz
    matriz -> float
    '''
    c = []
    for i in matriz:
        for j in i:
            c.append(j)
            return round(sum(c)/len(c),2)