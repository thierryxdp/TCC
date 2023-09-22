def acima_da_media(a):
    y = len(a)
    y1 = sum(a) / y
    y2 = a < y1
    return y2