def conta_frases(frases):
    str.replace(frases,'...','.',0,1)
    frases1 = str.count(frases,'?')
    frases2 = str.count(frases,'.')
    frases3 = str.count(frases,'!')
    return frases1 + frases2 + frases3