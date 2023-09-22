def pontos_por_time(l):
    """funcao que retorna os pontos por time em cada fase"""
    p1 = []
    p2 = []
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
    if l[1][2][0] == l[1][2][2]:
        list.append(p2,1)
        list.append(p1,1)
    return {l[0][0]:sum(p1),l[0][1]:sum(p2)}