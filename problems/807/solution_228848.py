def conta_frases(texto):
    """"""
    semreti=str.replace(texto, '...', '+')
    semexc=str.replace(semreti, '!', '+')
    seminterr=str.replace(semexc, '?', '+')
    semponto=str.replace(seminterr, '.', '+')
    frases=str.split(semponto, '+')
    del frases[-1]
    return len(frases)