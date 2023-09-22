#Start your python function here

def pontos_por_time(lista):
    """
    Essa função recebe uma lista de 2 elementos, que tem as 
    informações sobre dois jogos de futebol entre dois times
    e calcula o total de pontos de cada time, retornando um 
    dicionário com o <nome do time> -> <número total de pontos 
    na fase>
    list -> dict
    """
    placar_ida = lista[0][2]
    placar_volta = lista[1][2]
    a = []
    b = []
    c = []
    d = []
    for x in placar_ida:
        a.append(x)
        break
    for y in placar_ida:
        b.append(y)
    list.pop(b, 0)
    for z in placar_volta:
        c.append(z)
        break
    for e in placar_volta:
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
    if a > b and c > d:
        pontos_time_1 += 3
        pontos_time_2 += 3
    elif a < b and c > d:
        pontos_time_2 += 6
    elif a == b and c > d:
        pontos_time_1 += 1
        pontos_time_2 += 4
    elif a > b and c < d:
        pontos_time_1 += 6
    elif a > b and c == d:
        pontos_time_1 += 4
        pontos_time_2 += 1
    elif a == b and c == d:
        pontos_time_1 += 2
        pontos_time_2 += 2
    elif a < b and c < d:
        pontos_time_1 += 3
        pontos_time_2 += 3
    if pontos_time_1 >= pontos_time_2:
        return {time1: pontos_time_1, time2: pontos_time_2}
    elif pontos_time_2 > pontos_time_1:
    	return {time2: pontos_time_2, time1: pontos_time_1}