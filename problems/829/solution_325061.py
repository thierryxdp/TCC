def soma_h(N):
    h = 0
    i = 1 
    while i<=N:
        h += 1/i
        i+=1
    return round(h, 2)