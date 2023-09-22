def soma_h(N):
    denominador = range(1,N+1)
    H = 0
    for num in range(N):
        num = 1/denominador
        H += num
        denominador += 1
    return round(H, 2)