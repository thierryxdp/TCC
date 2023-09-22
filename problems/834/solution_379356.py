def media_matriz(m):
    i=0
    d=0
    for s in m:
        media=sum(m[i])/len(m[i])
        i=i+1
        d=d+media
        return d