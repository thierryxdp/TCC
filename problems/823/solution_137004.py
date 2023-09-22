def faltante(lista):
    l = lista
    l.sort()
    cont = 0
    peça = -1
    while cont < len(l):
        if l[cont] == cont + 1:
            cont += 1
        else:
            peça = cont +1 
            cont = len(l)
    if peça == -1:
        peça = len(l) + 1
    return peça