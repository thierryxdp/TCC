def pontos_por_time (l):
    '''função que recebe uma lista com o número de gols de dois times em dois jogos e analisa a quantidade de pontos que cada time fez. list -> dict'''
    pts_time1 = []
    pts_time2 = []
    if list[0][2][0] > list[0][2][1]:
           list.append(pts_time1,3)
    if list[0][2][0] < list[0][2][1]:
           list.append(pts_time2,3)
    if list[0][2][0] == list[0][2][1]:
           list.append (pts_time1,1)
           list.append (pts_time2,1)
    if list[1][2][0] > list[1][2][1]:
           list.append(pts_time2,3)
    if list[1][2][0] < list[1][2][1]:
            list.append(pts_time1,3)
    if list[1][2][0] == list[1][2][1]:
           list.append(pts_time1,1)
           list.append(pts_time2,1)
    return (list[0][0]:sum(pts_time1),list[0][1]:sum(pts_time2))