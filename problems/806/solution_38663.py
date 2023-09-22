def colisao(ret1,ret2):
    ret1 = tuple(xie1, yse1, xid1, ysd1) 
    ret2 = tuple(xie2, yse2, xid2, ysd2)
    if xid1<xie2:
        return False
    elif xid2<xie1:
        return False
    elif yse1<yse2 and ysd1<ysd2:
        return False
    elif yse2<yse1 and ysd2<ysd1:
        return False
    else:
        return True