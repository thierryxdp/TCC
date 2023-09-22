def media_matriz(m):
    med=0
    for l in m:
        for elemento in l:
            med = med+elemento
        conta=med/(len(m)*len(m[0]))
    return round(conta,2)