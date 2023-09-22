def media_matriz(matriz):
    '''funcao que calcula a media de todos os numeros de uma matriz com exatamente duas casas decimais;
    list -> float'''
    soma = 0
    media = 0
    for linha in matriz:
        for ijk in linha:
            soma += ijk
            media += soma/len(linha)
    return round(media,2)