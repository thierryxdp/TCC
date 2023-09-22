def soma_h(N):
    denominador = 1
    H = 0
    for num in N:
        num = 1/denominador
        H += num
        denominador += 1
    return round(H, 2)