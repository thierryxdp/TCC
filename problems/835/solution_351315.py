def melhor_volta(tempos):
    """recebe como entrada uma matriz que representa os tempos dos corredores e retorna de quem e qual e como foi a melhor volta;list -> tuple"""
    a=[]
    for x in tempos:
        for y in x:
            list.append(a,y)
            b=min(a)
    (list.index(tempos,x)+1,b,list.index(b,a)-(list.index(b,a)//10)*10)