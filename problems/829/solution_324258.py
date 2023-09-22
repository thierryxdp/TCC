def soma_h(n):
    r = []
    
    for i in range(1, n+1):
        r.append((1/i))
    round(sum(r), 2)
    return sum(r)