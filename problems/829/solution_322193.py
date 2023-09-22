def soma_h(n):
    h = 0
    a = 0
    for i in range(1,n+1):
        h = h + 1/(1+a)
        a = a + 1
    return h