def filtraMultiplos(x,n):
    indice = 0
    novalista = ()
    while indice < len(x):
        if x[indice]%n == 0:
            novalista += x[indice]
        indice += 1
    return novalista