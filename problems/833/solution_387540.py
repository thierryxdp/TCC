def conta_numero(numero,matriz):
    n = [numero]
    m  = matriz
    quantidade = 0
    for i in range(0, len(m)):
        if n in m[i]:
            quantidade += 1
    return quantidade