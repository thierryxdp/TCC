def media_matriz(m):
    a=range(len(m))
    b=range(len(m[0]))
    somadostermos=0
    parcela=[]
    
    for x in a:
        for y in b:
            parcela += [m[x][y]]
    somadostermos=sum(parcela)
    media=somadostermos/(len(m)*len(m[0]))
    return round(media,2)