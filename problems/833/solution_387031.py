def conta_numero(numero,matriz):
    r = []
    for i in range(len(matriz)):
        r = r + matriz[i]
    a = list.count(r,numero)
    return a