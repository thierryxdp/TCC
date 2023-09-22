def conta_frases(texto):
    pnto = str.split(texto,'.')
    excl = str.split(texto,'!')
    intr = str.split(texto,'?')
    retc = str.split(texto,'...')
    soma = list(pnto+excl+intr+retc)
    return soma