def conta_frases(texto):
    """"""
    semreti=str.replace(texto, '...', '  ')
    semexc=str.replace(semreti, '!', '  ')
    seminterr=str.replace(semexc, '?', '  ')
    return seminterr