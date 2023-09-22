def pontos_por_time(a):
    vencedor = []
    ptsa0=[]
    ptsa1=[]
    if a[0][2][0] > a[0][2][1]:
        ptsa0 = ptsa0 + 3
    if a[0][2][0] == a[0][2][1]:
        ptsa0 = ptsa0 + 1
        ptsa1 = ptsa1 + 1
    if a[0][2][0] < a[0][2][1]:
        ptsa1 = ptsa1 + 3
    if a[1][2][0] > a[1][2][1]:
        ptsa0 = ptsa0 + [3]
    if a[1][2][0] == a[1][2][1]:
        ptsa0 = ptsa0 + [1]
        ptsa1 = ptsa1 + [1]
    if a[1][2][0] < a[1][2][1]:
        ptsa1 = ptsa1 + [3]
    if ptsa0 > ptsa1:
        vencedor = vencedor +intptsa0
        return a[0][0], vencedor
    else:
        vencedor = vencedor + intptsa1
        return a[0][1], vencedor