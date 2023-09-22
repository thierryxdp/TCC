def conta_frases(texto):
    """"""
    semreti=str.replace(texto, '...', '  ')
    semexc=str.replace(semreti, '!', '  ')
    seminterr=str.replace(semexc, '?', '  ')
    semponto=str.replace(seminterr, '.', '  ')
    frases=str.split(semponto, '  ')
    list.remove(frases, '')
    return frases