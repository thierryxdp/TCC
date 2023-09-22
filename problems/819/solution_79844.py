def filtraMultiplos(n, i, j):
    contador = 1
    k= 0
    while contador<=n:
        if k%i==0 or k%j==0:
            contador = contador+1
            return k+1