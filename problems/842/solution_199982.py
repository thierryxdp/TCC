def pontos_por_time(l):
    classificacao = {l[0][0]: m, l[0][1]: n}
    if l[0][2][0] > l[0][2][1]:
        m = 0+3
        n = 0+0
    elif l[0][2][0] > l[0][2][1]:
        m = 0+1
        n = 0+1
    else:
        m = 0+0
        n = 0+3
    if l[1][2][0] > l[1][2][1]:
        m = m + 0
        n = n + 3
    elif l[1][2][0] > l[1][2][1]:
        m = m + 1
        n = n + 1
    else:
        m = m + 3
        n = n + 1
    return classificacao