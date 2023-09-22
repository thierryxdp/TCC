def colisao (tup1,tup2):
    if tup1[2] < tup2[0] or tup1 [0] > tup2[2] or tup1[3] < tup2[1] or tup1[1] > tup2[3]:
        return False
    else:
        True