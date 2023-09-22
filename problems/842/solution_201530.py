def pontos_por_time (l):
    v1 = 0
    v2 = 0
    e1 = 0
    e2 = 0
    n_de_pontost1 = 3*v1 + e1
    n_de_pontost2 = 3*v2 + e2
    if (l[0][2][0] > l[0][2][1]):
        v1= v1 + 1
    if (l[0][2][0] < l[0][2][1]):
        v2= v1 + 1
    if (l[0][2][0] == l[0][2][1]):
        e1= e1 + 1
        e2= e2 + 1
    if (l[1][2][1] > l[1][2][0]):
        v1= v1 + 1
    if (l[1][2][1] < l[1][2][0]):
        v2= v2 + 1
    if (l[1][2][1] == l[1][2][0]):
        e1= e1 + 1
        e2= e2 + 1
    return {l[0][0]:n_de_pontost1, l[0][1]:n_de_pontost2}