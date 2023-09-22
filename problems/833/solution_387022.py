def conta_numero(numero,matriz):
    r = []
    a = []
    for i in range(len(matriz)):
        r = r + matriz[i]
    if(numero in r):
        a = a + 1
    return a