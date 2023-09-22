def conta_frases(frases):
    str.replace(frases,'...','xy')str.replace(frases,'.','w')
    frases1 = str.count(frases,'?')
    frases2 = str.count(frases,'w')
    frases3 = str.count(frases,'!')
    frases4 = str.count(frases,'xy')
    return frases1 + frases2 + frases3 + frases4