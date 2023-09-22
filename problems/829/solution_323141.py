def soma_h(n):
    h = 0
    den = 1
    for i in range(0,n + 1):
        num = 1
        den = den + 1
        h += (num/den)
    return 1 + h