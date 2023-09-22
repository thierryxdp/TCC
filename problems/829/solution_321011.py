def soma_h(n):
    resultado = 0.00
    for c in range(n,1):
        a = 0.00
        for x in range(c, 0, -1):
            a = a + 1/n
        resultado = resultado + a
    return resultado