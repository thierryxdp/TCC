def pontos_por_time(ls):
    ls1=ls[0]
    ls2=ls[1]
    g1 = []
    g2 = []
    p1=ls1[2]
    p2=ls2[2]
    if p1[0] > p1[1]:
        g1 = [0, 3] 
    elif p1[0] < p1[1]:
        g1 = [3, 0]
    else:
        g1 = [1, 1]
    if p2[0] < p2[1]:
        g2 = [3, 0] 
    elif p2[0] > p2[1]:
        g2 = [0, 3]
    else:
        g2 = [1, 1]
    t = {ls[0][1]: (g1[1]+g2[0]), ls[0][0]: (g1[0]+g2[1])}
    return t