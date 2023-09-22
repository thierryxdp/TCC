def soma_h(n):
    h=0
    c=1
    for i in range(1, n+1):
            h = h+1/i
            c= c*1/i
    return h round(n,2)