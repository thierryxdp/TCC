def lingua_p(w):
    w=w.lower()
    vogais='aeiouáéíóúâêîôû'
    for c in vogais:
        w=str.replace(w,c,c+'p'+c)
    return w