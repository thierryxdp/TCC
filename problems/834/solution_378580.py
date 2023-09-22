def media_matriz (matriz):
    '''Dada uma matriz de inteiros não vazia, retorne a média
       de todos os números da matriz;
       list -> float'''
    componentes = 0
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma = soma+matriz[i][j]
            componentes = componentes +1
    media = soma /componentes
    return round(media,2)