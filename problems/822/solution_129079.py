def repetidos(x):
    r = 0
    ft = x[1:len(x)]
    for s in range(len(ft)):
        if x[s]==ft[s]:
            r = r+1
    return r