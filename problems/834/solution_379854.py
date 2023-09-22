def media_matriz(m):
    a=0
    b=0
    c=0
    for i in m:
        for j in i:
            a+=j
            c+=1
    b=a/c
    return b