def conta_numero(numero,matriz):
    m=len(matriz)
    n=len(matriz[0])
    cont=0
    for i in range(m):
        for j in range(n):
            if numero in range(i):
                cont=cont+1
            if numero in range(m):
                cont=cont+1
    return cont