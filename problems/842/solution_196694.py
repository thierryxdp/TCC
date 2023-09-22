#Start your python function here

def pontos_por_time(lista):
    placar_1_fase = lista[0][2]
    placar_2_fase = lista[1][2]
    a = []
    b = []
    c = []
    d = []
    for x in placar_1_fase:
        a.append(x)
        break
    for y in placar_1_fase:
        b.append(y)
    list.pop(b, 0)
    for z in placar_2_fase:
        c.append(z)
        break
    for e in placar_2_fase:
        d.append(e)
    list.pop(d, 0)
    str_a = [str(u) for u in a]
    aa = "".join(str_a)
    a = int(aa)
    
    str_b = [str(p) for p in b]
    bb = "".join(str_b)
    b = int(bb)
    
    str_c = [str(i) for i in c]
    cc = "".join(str_c)
    c = int(cc)
    
    str_d = [str(t) for t in d]
    dd = "".join(str_d)
    d = int(dd)
    
    time1 = lista[0][0]
    time2 = lista[1][0]
    pontos_time_1 = 0
    pontos_time_2 = 0
    while True:
        if a > b:
            pontos_time_1 += 3
        elif b > a:
            pontos_time_2 += 3
        elif a == b:
            pontos_time_1 += 1
            pontos_time_2 += 1
        elif c > d:
            pontos_time_2 += 3
        elif d > c:
            pontos_time_1 += 3
        elif c == d:
            pontos_time_1 += 1
            pontos_time_2 += 1
        break
    return {time1: pontos_time_1, time2: pontos_time_2}