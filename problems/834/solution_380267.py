def media_matriz(matriz):
    '''funçao que calcula a media da matriz com duas casas decimais de precisao'''
    soma = 0
    tam = 0
    for linha in matriz:
        soma += sum(linha)
        tam += len(linha)
    return round((soma/tam), 2)