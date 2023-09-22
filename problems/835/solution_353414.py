def melhor_volta(m):
    a=0
    b=0
    c=0
    menor=min(m)
    for i in range(len(m)):
        if menor==m[i]:
            a=i
    for j in range(len(menor)):
        b=min(menor)
        if b ==menor[i]:
            c=i
    return (a,b,c)