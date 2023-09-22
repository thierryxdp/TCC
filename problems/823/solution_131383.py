def faltante(lista):
    lista.sort()
    x=0
    n=1
    while x < len(lista):
        if n in lista == False:
            return n
        else:
            n=n+1
        x=x+1