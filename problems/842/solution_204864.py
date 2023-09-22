def pontos_por_time(lista):
    """recebe uma lista com o numero de gols de dois times em dois jogos e analisa a quantidade de pontos que cada time fez
    list -> dict"""
    p.time1 =[]
    p.time2 =[]
    if lista[0][2][0] > lista[0][2][1]:
        list.append(p.time1,3)
    if l[0][2][0] < l[0][2][1]:
        list.append(p.time2,3)
    if lista[0][2][0] == lista[0][2][1]:
        list.append(p.time1,1)
        list.append(p.time2,1)
    if lista[1][2][0] > lista[1][2][1]:
        list.append(p.time2,3)
    if lista[1][2][0] < lista[1][2][1]:
        list.append(p.time1,3)
    if lista[1][2][0] == lista[1][2][1]:
        list.append(p.time1,1)
        list.append(p.time2,1)
    return {l[0][0]:sum(p.time1),l[0][1]:sum(p.time2)}