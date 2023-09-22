def faltante(lista):
    nl = lista[:]
    nl.sort()
    peca = 0
    for n,v in enumerate(lista):
        if v != n+1:
            peca = n+1
            
    if peca == 0:
        peca = len(nl) +1
    return peca