def media_matriz(m):
    i=0
    a=0
    d=0
    for s in m:
    	a+=sum(m[i])
    	d+=len(m[i])
        i=i+1
    return a/d