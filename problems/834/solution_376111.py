def media_matriz(matriz):
    '''Função calcula e retorna a média de todos os numeros de uma matriz;
    matriz -> float'''
    soma = 0

    for i in matriz:
        soma += sum(i)
    media = soma/(len(matriz)*len(matriz[0]))

    return round(media,2)