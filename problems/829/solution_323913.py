def soma_h(N):
    valorH = 0
    for i in range(1, N):
        inverso = (1/i)
        valorH = valorH + inverso
    return valorH