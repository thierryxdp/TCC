def faltante(lista):
    l = lista[:]
    l.sort()
    cont = 0
    peca = -1
    while cont < len(l):
        if l[cont] == cont + 1:
            cont+1
        elif:
            peca = cont+1
            cont= len(l)
        elif peca == -1:
        peca = len(l)+1
    return peca