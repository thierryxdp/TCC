from math import ceil
def melhor_volta(m):
    a=m[0]
    b=m[1]
    c=m[2]
    d=m[3]
    e=m[4]
    f=m[5]
    g=a+b+c+d+e+f
    minimo=min(g)
    g.index(minimo)
    return (ceil((g.index(minimo))/6,minimo=min(g),(g.index(minimo)%6)+1)