def conta_frases(texto):
    texto=texto.format('...','!')
    texto=texto.format('?','!')
    texto=texto.format('.','!')
    frases=texto.split('!')
    return len(frases)