def media_matriz(m):
    ''' retorna a media de todos os numeros da matriz informada
    list(list) -> float'''
    
    num = []
    
    for i in m:
        for j in i:
            num += [j,]
    
    media = sum(num)/len(num)
    return round(media,2)