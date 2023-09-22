def media_matriz(m):
    divisor = 0
    somas = 0
    somas2 = 0
    for i in m:
        for z in m[i]:
            somas = somas + m[i][z]
            divisor = divisor + 1
    somas2 = somas/divisor
    return somas2