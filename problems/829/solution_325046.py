def soma_h(n):
    r = []
    for i in list(range( 1, n + 1)):
        r.append(1/i)
    r = sum(r)
    r = round(r, 2)
    
    return r