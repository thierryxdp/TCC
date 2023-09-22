def conta_frases(texto):
    """"""
    semreti=str.replace(texto, '...', '   ')
    semexc=str.replace(semreti, '!', '   ')
    seminterr=str.replace(semexc, '?', '   ')
    semponto=str.replace(seminterr, '.', '   ')
    semdoispontos=str.replace(semponto, ':', '   ')
    frases=str.split(semdoispontos, '   ')
    del frases[-1]
    return len(frases)