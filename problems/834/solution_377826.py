def media_matriz(matriz):
    '''retorna a media dos numeros da matriz
    matriz -> float
    '''
    m = []
    for i in matriz:
        for j in i:
            m.append(j)
    return round(sum(m)/len(m),2)