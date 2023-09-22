def conta_frases(texto):
    pontos = '.','!','?','...'
    pnto = str.join(texto,'.')
    excl = str.split(texto,'!')
    intr = str.split(texto,'?')
    retc = str.split(texto,'...')
    return pnto+excl