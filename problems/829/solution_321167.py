def soma_h(n):
    i = 0
    d=1/n
    for n1 in range(1,n+1):
        fat=1
        for n2 in range(n1,0,n+1):
            fat=fat+n2
        i = i + fat
        return i