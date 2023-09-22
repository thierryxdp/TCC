def pontos_por_time(a):
    b = a[0]
    c = a[1]
    b2 = b[2]
    c2 = c[2]
    pc = 0
    pf = 0
    if b2[0] > b2[1]:
        pc = pc + 3
    elif b2[0] == b2[1]:
        pc = pc + 1
        pf = pf + 1
    if c2[0] > c2[1]:
        pc = pc + 3
    elif c2[0] == c2[1]:
        pc = pc + 1
        pf = pf + 1
    x = {b[0]:pc,b[1]:pf}
    return x