def conta_frases(texto):
    pontos = '.','!','?','...'
    pnto = len(str.split(texto,'.'))
    excl = str.split(texto,'!')
    intr = str.split(texto,'?')
    retc = str.split(texto,'...')
    return str.replace(texto,'.','')