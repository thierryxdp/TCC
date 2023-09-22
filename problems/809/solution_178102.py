def intercala(lista1, lista2):
    if len(lista1) == 0:
        return []
    def ligar(lista1, list2):
        if len(l2) == 0:
            return []
        return [ (h1, l2[0])] + ligar(h1,l2[1:])

    return ligar(lk1[0], lk2) + intercala(lk1[1:], lk2)