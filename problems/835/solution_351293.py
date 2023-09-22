def melhor_volta(tempos):
    """recebe como entrada uma matriz que representa os tempos dos corredores e retorna de quem e qual e como foi a melhor volta;list -> tuple"""
    a=[1,2,3,4,5,6]
    b=[1,2,3,4,5,6,7,8,9,10]
    c=[]
    d=[]
    for x in a:
        for y in b:
            c=c+[(a,tempos[x-1][b-1],b)]
    for l in tempos:
        for m in l:
            d=d+m
            f=min(d)
            w=list.index(d,f)
    return c[w]