def conta_frases(frase):
    QtFrases = 1
    
    if '.' in frase:
        QtFrases = QtFrases + int(frase.count('.'))
    if '...' in frase:
        QtFrases = QtFrases + int(frase.count('...'))
    if '!' in frase:
        QtFrases = QtFrases + int(frase.count('!'))
    if '?' in frase:
        QtFrases = QtFrases + int(frase.count('?'))
    
    return QtFrases