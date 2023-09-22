def filtraMultiplos(l,n):
    lista = l[:]
    contador = 0
    while contador<len(l):
        if l[contador]%n==0:
            contador = contador + 1
        else:
            return l