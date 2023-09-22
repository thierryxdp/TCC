def media_matriz(matriz):
    '''Recebe uma matriz e retorna a media de todos os numeros dentro dela, com duas casas
    decimais de precisao
    matriz -> float'''
    n_elem=0
    soma_elem=0
    for lista in matriz:
        for elem in lista:
            soma_elem= soma_elem+elem
            n_elem=n_elem+1
    media= soma_elem/n_elem
    return round(media,2)