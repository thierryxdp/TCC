def conta_frases(texto):
    str = '.','!','?','...'
    pnto = str.split(texto,'.')
    excl = str.split(texto,'!')
    intr = str.split(texto,'?')
    retc = str.split(texto,'...')
    return str.split(texto,0)