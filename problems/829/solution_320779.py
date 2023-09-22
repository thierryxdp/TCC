def soma_h(n):
    h = 0
    for a in list(range(n+1))[1::]:
        h += 1/a 
    return round(h,2)