def conta_frases(txt):
    return txt.count('.')+txt.count('?')-2*txt.count('...')+txt.count('!')