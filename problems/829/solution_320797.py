def soma_h(N):
    somaH = 0
    for i in range(1,N + 1):
        somaH += 1/i
    return round(somaH,2)