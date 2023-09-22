def conta_numero (matriz, n):
    contador = 0
    for i in matriz:
        contador += i.count(n)
    return contador