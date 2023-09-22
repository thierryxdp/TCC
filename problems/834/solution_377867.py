def media_matriz(matriz):
    """A funcao calcula e retorna a media de todos os numeros
	de uma matriz; list(list)-->float"""
    i=0
    soma=0
    for linha in matriz:
        soma+=sum(linha)
        i+=len(linha)
                      
    return round((soma/i),2)