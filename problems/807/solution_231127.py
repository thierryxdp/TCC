def conta_frases(frases):
    frases_nova=str.replace(frases,'...','$')
    ponto=str.count(frases_nova,'.')
    exclamacao=str.count(frases_nova,'!')
    interrogacao=str.count(frases_nova,'?')
    reticencias=str.count(frases_nova,'...')
    retic=str.count(frases_nova,'$')
    frases1=ponto+exclamacao+interrogacao+retic
    return frases1