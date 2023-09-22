def conta_numero(numero,matriz):
    c=0
    sq= 0
    for sq in range(len(matriz)):
        contador = matriz[sq].count(numero)
        c+=contador
    return c