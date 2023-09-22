def pontos_por_time(l):
    if l[0][2][0] > l[0][2][1]:
        p1 = 3
        P1 = 0
    elif l[0][2][0] > l[0][2][1]:
        p1 = 1
        P1 = 0
    else:
        p1 = 0
        P1 = 3
    if l[1][2][0] > l[1][2][1]:
        p2 = 0
        P2 = 3
    elif l[1][2][0] > l[1][2][1]:
        p2 = 1
        P2 = 1
    else:
        p2 = 3
        P2 = 0
    return classificacao = {l[0][0]:p1 + p2, l[0][1]:P1 + P2}