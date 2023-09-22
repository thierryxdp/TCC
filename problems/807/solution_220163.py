def conta_frases(frase):
    QtFrases = 0
    
    if '.' in frase:
        QtFrases = QtFrases + int(frase.count('.'))
    if '...' in frase:
        frase.replace('...','+')
        QtFrases = QtFrases + int(frase.count('+'))
    if '!' in frase:
        QtFrases = QtFrases + int(frase.count('!'))
    if '?' in frase:
        QtFrases = QtFrases + int(frase.count('?'))
    
    return QtFrases