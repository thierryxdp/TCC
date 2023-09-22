def soma_h(N):
    H = 1
    n = round(N,2)
    for i in range(1, n):
        if i in n:
            H = H + (1//i)
    return H