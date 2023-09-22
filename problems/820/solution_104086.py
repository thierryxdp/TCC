def posLetra(frase, n, x):
    for h in frase:
        if h == n:
            return frase.find(n)