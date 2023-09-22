def media_matriz(matriz:list)->float:
    """Dada uma determinada matriz, retorna a média aritmética de todos os elementos contidos nela."""
    soma=0
    total_elementos=len(matriz)*len(matriz[0])
    for linha in range(len(matriz)):
        soma+=sum(matriz[linha])
    media=soma/total_elementos
    return round(media,2)