def media_matriz(m):
    total = 0
    e = 0
    for i in m:
        total = total + sum(i)
        e = e + len(i)
    return round(total/e,2)