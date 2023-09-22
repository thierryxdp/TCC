def media_matriz(m):
    i=0
    d=0
    for s in m:
        media=sum(m[i])/len(m[i])
        d=d+media
        i=i+1
    return d