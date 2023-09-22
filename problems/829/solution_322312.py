def soma(N):
    'somatorio de 1/1 até 1/N int -> float'
    H = 0
    x = 1
    while (x<=N):
        H = H+(1/x)
        x = x+1
    return: H