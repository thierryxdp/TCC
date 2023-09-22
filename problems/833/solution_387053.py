def conta_numero (matriz, n):
    contador = 0
    for i in matriz:
        contador += 1.count(n)
    return contador