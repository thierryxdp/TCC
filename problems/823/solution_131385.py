def faltante(lista):
    lista.sort()
    x=0
    n=1
    while x < len(lista):
        if n in lista:
            n=n+1
        else:
            return n
        x=x+1