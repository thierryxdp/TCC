def conta_numero(n, A):
    cont = 0
    for elemento in A:
        if elemento == n:
            cont += 1
    return cont