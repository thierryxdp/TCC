def conta_frases(frases):
    frases2 = str.count(frases,'...')
    str.replace(frases,'.','z') 
    frases1 = str.count(frases,'?')
    frases3 = str.count(frases,'!')
    return frases1 + frases2 + frases3