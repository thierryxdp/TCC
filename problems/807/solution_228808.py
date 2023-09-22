def conta_frases(texto):
    """"""
    semreti=texto.replace('...', ' ')
    semponto=semreti.replace('.', ' ')
    seminter=semponto('?', ' ')
    semexc=seminter('!', ' ')
    frases=semexc.split()
    return len(frases)