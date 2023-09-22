def conta_frases(frases):
    str.replace(frases,'...','xy')
    frases1 = str.count(frases,'?')
    frases2 = str.count(frases,'.')
    frases3 = str.count(frases,'!')
    frases4 = str.count(frases,'xy')
    return frases1 + frases2 + frases3 + frase4