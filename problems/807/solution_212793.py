def conta_frases(texto):
    pontos = '.','!','?','...'
    pnto = str.split(texto,'.')
    excl = str.split(texto,'!')
    intr = str.split(texto,'?')
    retc = str.split(texto,'...')
    return pontos