def pontos_por_time(ls):
    ls1=ls[0]
    ls2=ls[1]
    g1 = []
    g2 = []
    if ls1[0][2][0] > ls1[0][2][1]:
        g1 = [0, 3] 
    elif ls1[0][2][0] < ls1[0][2][1]:
        g1 = [3, 0]
    else:
        g1 = [1, 1]
    if ls2[1][2][0] < ls2[1][2][1]:
        g2 = [3, 0] 
    elif ls2[1][2][0] > ls2[1][2][1]:
        g2 = [0, 3]
    else:
        g2 = [1, 1]
    t = {ls[0][1]: (g1[1]+g2[0]), ls[0][0]: (g1[0]+g2[1])}
    return t