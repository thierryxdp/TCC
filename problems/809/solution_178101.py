def intercala(lk1, lk2):
    if len(lk1) == 0:
        return []
    def ligar(h1, l2):
        if len(l2) == 0:
            return []
        return [ (h1, l2[0])] + ligar(h1,l2[1:])

    return ligar(lk1[0], lk2) + intercala(lk1[1:], lk2)