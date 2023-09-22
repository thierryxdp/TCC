def conta_numero(numero,matriz):
    r = []
    a = 0
    for i in range(len(matriz)):
        r = r + matriz[i]
    for b in range(len(r)):
        if(numero in r):
            a+=1
    return a