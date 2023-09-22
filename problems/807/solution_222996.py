def conta_frases(texto):
    """Dado um texto qualquer, na qual todas as frases são separadas por pontos
    ('.','!','?','...'), onde não há pontos iguais consecutivos, como ('!!!' ou '??'):
    str-->int"""
    frases=texto.replace('!','.').replace('?','.').replace('...','.').split('.')
    return len(frases)-1