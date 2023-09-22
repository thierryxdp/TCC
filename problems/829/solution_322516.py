def soma_h(N):
    acumulador = 0
    for x in range(1, N+1):
        acumulador = acumulador + 1/x
    return round(acumulador, 2)