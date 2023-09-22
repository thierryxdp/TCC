def media_matriz(m):
    a=[]
    for l in range(len(m)):
        for c in range(len(m[0])):
            a.append(m[l])
            z=sum(a)/len(m[0])+len(m)
    return round(z,2)