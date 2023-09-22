def faltante(lista):
    lista.sort()
    x=0
    n=1
    while x < len(lista+1):
        if n in lista:
            n=n+1
        else:
            return n
        x=x+1