def soma_h(N):
    H = 1
    for i in range(1, N):
        if i in round(N, 2):
            H = H + (1//i)
    return H