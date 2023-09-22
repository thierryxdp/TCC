def conta_frases(texto):
    pnto = list(str.split(texto,'.'))
    excl = list(str.split(texto,'!'))
    intr = list(str.split(texto,'?'))
    retc = list(str.split(texto,'...'))
    return retc