def soma_h(N):
    x = 1
    k = 0
    while x < N + 1:
        k = k + 1/x
        x = x + 1
    k = round(k,2)
    return k