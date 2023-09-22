def soma_h(N):
    H = 1
    for i in range(N):
        if i in N:
            H = H + (1//i)
    return H