def conta_frases(frases):
    frases1 = str.count(frases,'?')
    frases2 = str.count(frases,'.')
    frases3 = str.count(frases,'!')
    frases4 = str.count(frases,'...')
    return frases1 + frases2 + frases3 + frases4