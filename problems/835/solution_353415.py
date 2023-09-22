def melhor_volta(m):
    a=0
    b=0
    c=0
    menor=min(m)
    for i in range(len(m)):
        if menor == m[i]:
            a=i
    return a