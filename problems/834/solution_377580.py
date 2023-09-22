def media_matriz(matriz):
    """A funcao calcula e retorna a media de todos os numeros
	de uma matriz; list-->float"""
    i=0
    soma=0
    for linha in matriz:
        for element in linha:
            soma+=element         
    return soma/len(matriz)