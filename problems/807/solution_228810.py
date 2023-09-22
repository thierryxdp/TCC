def conta_frases(texto):
    """"""
    semreti=texto.replace('...', ' ')
    frases=semreti.split()
    return len(frases)