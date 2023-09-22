def media_matriz(matriz):
    '''funcao que calcula a media de todos os numeros de uma matriz com exatamente duas casas decimais;
    list -> float'''
    soma = 0
    media = 0
    for linha in matriz:
        soma += sum(linha)
    media = soma/ len(matriz)
    return round(media,2)