def conta_frases(texto):
    pontos = '.','!','?','...'
    pnto = str.join(texto,'.')
    excl = str.join(texto,'!')
    intr = str.split(texto,'?')
    retc = str.split(texto,'...')
    return pnto+excl