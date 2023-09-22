def media_matriz(matriz):
    """retorna a media de todos o numeros da matriz
    list -> int"""
    m=[]
    for l in matriz:
        for c in l:
            m.append(c)
    media=sum(m)/len(m)
    return round(media,2)