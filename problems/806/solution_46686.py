def colisao(tup1, tup2):
    x1 = tup1[0]
    y1 = tup1[1]
    x2 = tup1[2]
    y2 = tup1[3]
    x3 = tup2[0]
    y3 = tup2[1]
    x4 = tup2[2]
    y4 = tup2[3]
    if ((x2 < x3) or (x4 < x1) or (y2 < y3) or (y4 < y1)):
        return 'False'
    else:
        return 'True'