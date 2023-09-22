def conta_frases(frases):
    reticencias=str.replace(frases,'...','.')
    ponto=str.count(reticencias,'.')
    exclamacao=str.count(frases,'!')
    interrogacao=str.count(frases,'?')

    quantidade=ponto+exclamacao+interrogacao
    return quantidade