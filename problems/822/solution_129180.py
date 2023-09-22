def repetidos(l):
    nl = []
    prox = 0
    while prox < len(l):
        if l[prox] == l[prox - 1]:
            nl.append(prox)
        prox += 1
    fim = len(nl)
    return fim