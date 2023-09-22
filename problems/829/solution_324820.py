def soma_h(n):
    h = 0
    contagem = 0
    limit = n + 1
    while contagem < limit:
        if contagem > 0:
            h += 1 / contagem
        contagem += 1
    h = round(h, 2)
    return h