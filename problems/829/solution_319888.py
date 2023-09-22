def somaFraçoes(n):
    H = 0
    for N in range (1,n+1):
        H = H + (1/N)
    return H