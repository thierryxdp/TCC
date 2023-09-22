def soma_h(n):
    h = []
    for i in range(1,n+1):
        h.append(1/i)
    return round(sum(h), 2)