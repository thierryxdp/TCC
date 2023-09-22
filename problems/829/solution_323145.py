def soma_h(n):
    h = 0
    den = 0
    for i in range(n):
        num = 1
        den = den + 1
        h += (num/den)
    return round(h,2)