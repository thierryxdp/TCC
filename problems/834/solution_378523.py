def media_matriz(m):
    divisor = 0
    somas = 0
    somas2 = 0
    prox = 0
    for i in m:
        for z in m[prox]:
            somas = somas + z
            divisor = divisor + 1
        prox = prox + 1
    somas2 = somas/divisor
    somas3 = round(somas2, 2)
    return somas3