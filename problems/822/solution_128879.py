def repetidos(ls):
    x = 0
    rp=ls[1:len(ls)]
    for i in range(len(rp)):
        if ls[i] == rp[i]:
            x= x + 1
    return x