def soma_h(n):
    contagem = 0
    for i in range(1, n + 1):
        contagem += 1/i
    return round(contagem, 2)