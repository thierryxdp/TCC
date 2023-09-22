def pontos_por_time(a):
    vencedor = []
    ptsa0=[]
    ptsa1=[]
    if a[2][0] > a[2][1]:
        ptsa0 = ptsa0 + 3
    if a[2][0] == a[2][1]:
        ptsa0 = ptsa0 + 1
        ptsa1 = ptsa1 + 1
    if a[2][0] < a[2][1]:
        ptsa1 = ptsa1 + 3
    if [5][0] > [5][1]:
        ptsa0 = ptsa0 + 3
    if a[5][0] == a[5][1]:
        ptsa0 = ptsa0 + 1
        ptsa1 = ptsa1 + 1
    if a[5][0] < a[5][1]:
        ptsa1 = ptsa1 + 3
    if ptsa0 > ptsa1:
        vencedor = vencedor + ptsa0
        return a[0], vencedor
    else:
        vencedor = vencedor + ptsa1
        return a[1], vencedor