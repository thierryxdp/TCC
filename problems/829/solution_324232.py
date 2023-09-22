def soma_h(x):
    r = 0
    for i in range(1, x+1):
        if x>0:
            r = r + 1/i
    return round(r, 2)