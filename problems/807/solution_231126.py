def conta_frases(frases):
    ponto=str.count(frases,'.')
    exclamacao=str.count(frases,'!')
    interrogacao=str.count(frases,'?')
    reticencias=str.count(frases,'...')
    frases1=ponto+exclamacao+interrogacao+reticencias
    return frases1