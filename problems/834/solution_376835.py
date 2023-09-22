def media_matriz(m):
    a=[]
    for l in range(len(m)):
        for c in range(len(m[0])):
            a.append(m[l][c])
            z=sum(a)/len(m[c])
    return round(z,2)