def media_matriz(m):
    i=0
    for s in m:
        media=(sum(m[i])+sum(m[0][i]))/(len(m)+len(m[0]))
        i=i+1
    return media