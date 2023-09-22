def conta_frases(texto):
    texto=texto.format('...','!')
    texto=texto.format('?','!')
    texto=texto.format('.','!')
    frases=texto.split('!')
    print frases
    return len(frases)