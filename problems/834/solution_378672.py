def media_matriz(matriz):
    '''
    '''
    if matriz == []:
        return ' matriz vazia '
    
    soma=0
    divisor=0
    media_matriz=0
    for linha in matriz:
        soma= soma+ sum(linha)
        divisor= divisor+ len(linha)
    media_matriz= media_matriz+(soma/divisor)

    return round(media_matriz,1)