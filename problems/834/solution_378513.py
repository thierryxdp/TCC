def media_matriz(m):
    divisor = 0
    somas = 0
    somas2 = 0
    prox = 0
    for i in m:
        prox = prox + 1
        for z in m[prox]:
            somas = somas + z
            divisor = divisor + 1
    somas2 = somas/divisor
    return somas2