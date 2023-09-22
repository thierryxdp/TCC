def acima_da_media(a):
    y = len(a)
    y3 = range(y)
    y1 = int(sum(a) / y)
    y2 = a < y1
    return y3