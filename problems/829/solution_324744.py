def soma_h(n):
    h = 0
    i = 1
    for i in range(n):
        h += 1/(i+1)
        i += 1
    return round(h,2)