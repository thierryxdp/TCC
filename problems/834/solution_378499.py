def media_matriz(m):
    "Retorne a média da matriz dada; lista(lista)->int"
    qe=len(m)*len(m[0])
    s=[]
    for i in m:
        for j in i:
            s.append(j)
    return round(sum(s)/qe,2)