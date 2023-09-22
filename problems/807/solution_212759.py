def conta_frases(texto):
    pnto = str.split(texto,'.')
    excl = str.split(pnto,'!')
    intr = str.split(excl,'?')
    retc = str.split(intr,'...')
    return len(pnto)