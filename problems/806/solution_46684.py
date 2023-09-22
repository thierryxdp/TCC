def colisao(tup1, tup2):
    if len(tup1)==4 and len(tup2)==4 and tup1(2) < tup2(0) or tup2(2) < tup1(0) or tup1(3) < tup2(1) or tup2(3) < tup1(1):
        return 'false'
    else:
        return 'true'