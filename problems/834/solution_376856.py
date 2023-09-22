def media_matriz(m):
    elementos = len (m[0]) * len(m)
    elementos_2 = 0
    for l in m:
        for j in l:
            elementos_2 += j
    media = elementos_2/elementos
    return round(media,2)