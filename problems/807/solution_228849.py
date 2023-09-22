def conta_frases(texto):
    """Esta funcao recebe um texto e conta quantas frases ele tem.
    Entrada: str
    Saida: int"""
    semreti=str.replace(texto, '...', '+')
    semexc=str.replace(semreti, '!', '+')
    seminterr=str.replace(semexc, '?', '+')
    semponto=str.replace(seminterr, '.', '+')
    frases=str.split(semponto, '+')
    del frases[-1]
    return len(frases)