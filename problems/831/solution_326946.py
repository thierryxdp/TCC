def lingua_p(p):
    p.lower()
    p2=p
    for i in p:
        if i in "aeiouáéíóúãõ":
            p2=p2[:p2.index(i)]+i+"p"+p2[p2.index(i):]
    return p2