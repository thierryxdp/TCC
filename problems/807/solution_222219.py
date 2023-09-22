def conta_frases(frases):
    return str.count(frases,'.') - 2*(str.count(frases,'.')) + str.count(frases,'?') + str.count(frases,'!')