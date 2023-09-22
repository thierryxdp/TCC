def media_matriz(matriz):
    '''funcao que pega uma matriz de numeros inteiros e retorna a media deles
    int -> float'''
    mean = []
    for i in matriz:
        for n in i:
            mean.append(n)
    return round((sum(mean)/len(mean)), 2)