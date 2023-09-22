def pontos_por_time(lista,p.t1,p.t2):
    """recebe uma lista com o numero de gols de dois times em dois jogos e analisa a quantidade de pontos que cada time fez
    list -> dict""" 
    p.t1 = []
    p.t2 =[]
    if list[0][2][0] > list[0][2][1]:
        list.append(p.t1,3)
    if list[0][2][0] < list[0][2][1]:
        list.append(p.t2,3)
    if list[0][2][0] == list[0][2][1]:
        list.append(p.t1,1)
        list.append(p.t2,1)
    if list[1][2][0] > list[1][2][1]:
        list.append(p.t2,3)
    if list[1][2][0] < list[1][2][1]:
        list.append(p.t1,3)
    if list[1][2][0] == list[1][2][1]:
        list.append(p.t1,1)
        list.append(p.t2,1)
    return (list[0][0]:sum(p.t1),list[0][1]:sum(p.t2))