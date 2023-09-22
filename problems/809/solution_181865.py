def intercala(l1,l2):
    res = l1 + l2
    res[::2] = l1
    res[1::2]= l2
    return res