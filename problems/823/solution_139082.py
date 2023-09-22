def faltante(ls):
    ls.sort

    for e in range(len(ls)):
        if ls[e]-2 == ls[e-1]:
            return ls[e]-1