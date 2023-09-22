def media_matriz(m):
    ''' retorna a media de todos os numeros da matriz informada
    list(list) -> float'''
    
    num = []
    
    for i in m:
        for j in i:
            num += [j,]
    
    media = round(sum(num)/len(num),2)
    return media