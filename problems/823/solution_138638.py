def faltante(lista):
    nl = lista[:]
    nl.sort()
    for n,v in enumerate(lista):
        if v != n+1:
            return n+1
    return len(lista)+1