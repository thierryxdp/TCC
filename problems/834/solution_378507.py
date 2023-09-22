def media_matriz(m):
    divisor = 0
    somas = 0
    somas2 = 0
    prox = 0
    prox2 = 0
    for i in m:
        prox = prox + 1
        prox2 = 0
        for z in m[prox]:
            somas = somas + m[prox][prox2]
            divisor = divisor + 1
            prox2 = 0
    somas2 = somas/divisor
    return somas2