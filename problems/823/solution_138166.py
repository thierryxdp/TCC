def faltante(lista):
    falta=len(lista)+1
    n=1
    i=0
    while i<=falta:
        if n==falta:
            return n
        elif n!=lista[i]:
            return n
        n=n+1
        i=i+1