def media_matriz(n):
    i=0
    p=0
    while i<len(n):
        p=sum(n[i])+p
        i=i+1
    return round(p/(len(n[0])*len(n)))