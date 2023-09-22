def media_matriz(matriz):
    """
"""
    media=[]
    sequencia=0
    contagem=0
    for sequencia in range(len(matriz)):
        
        for sequencia in range(len(matriz[sequencia])):
            media.append(matriz[sequencia])
    return round(sum(media)/len(media),2)