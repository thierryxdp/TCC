def fatorial(N):
    F = 1
    if N == 0:
        return 1
    while N != 0:
        F = F * N
        N = N - 1
    return F