def posLetra(palavra, letra, num):
    n_letra = 0
    i = 0
    pos = -1
    l = list(palavra)
    while i < len(l):
        if l[i] == letra:
            n_letra += 1
            if n_letra == num:
                pos=i
        i += 1
    return pos