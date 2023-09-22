def melhor_volta(tempos):
    """recebe como entrada uma matriz que representa os tempos dos corredores e retorna de quem e qual e como foi a melhor volta;list -> tuple"""
    a=[]
    for x in tempos:
        for y in x:
            list.append(a,y)
    t=min(a)+1
    c=list.index(a,t)//10
    v=list.index(a,t)-c*10
    return (c,t,v)