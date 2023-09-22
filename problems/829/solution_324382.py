def soma_h(n):
    ls = []
    for e in range(1, n+1):
        ls.append (1/e)
    return round(sum(ls), 2)