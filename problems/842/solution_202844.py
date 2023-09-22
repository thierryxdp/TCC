def pontos_por_time(l):
    """recebe uma lista com o numero de gols de dois times em dois jogos e analisa a quantidade de pontos que cada time fez
    list -> dict""" 
    p1 = []
    p2 =[]
    if l[0][2][0] > l[0][2][1]:
        list.append(p1,3)
    if l[0][2][0] < l[0][2][1]:
        list.append(p2,3)
    if l[0][2][0] == l[0][2][1]:
        list.append(p1,1)
        list.append(p2,1)
    if l[1][2][0] > l[1][2][1]:
        list.append(p2,3)
    if l[1][2][0] < l[1][2][1]:
        list.append(p1,3)
    if l[1][2][0] == l[1][2][1]:
        list.append(p1,1)
        list.append(p2,1)
    return {"cormengo":sum(p1),"flaminthians":sum(p2)}