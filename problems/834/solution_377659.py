def media_matriz(m):
    """funcao que dada uma matriz retorna a media de todos os elementos.
    list-->floot"""
    media=0
    for i in range(len(m)):
        for j in range(len(m[0])):
            media+=m[i][j]
    return round(media/(len(m)*len(m[0])),2)