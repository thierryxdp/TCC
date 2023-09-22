def media_matriz(m):
    elementos=len(m[0])*len(m)
    s_elementos=0
    for l in m:
        for j in l:
            s_elementos+=j
    media=s_elementos/elementos
    return media