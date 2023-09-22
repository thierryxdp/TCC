def conta_frases(frases):
    ponto=str.count(frases,'.')
    exclamação=str.count(frases,'!')
    interrogação=str.count(frases,'?')
    reticências=str.count(frases,'...')
    frases1=ponto+exclamação+interrogação+reticências
    return frases1