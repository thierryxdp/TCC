def conta_frases(frase):
    QtFrases = 0
    
    if '...' in frase:
        frase.replace('...','+')
    elif '+' in frase:
        QtFrases = QtFrases + int(frase.count('+'))
    elif '.' in frase:
        QtFrases = QtFrases + int(frase.count('.'))
    elif '!' in frase:
        QtFrases = QtFrases + int(frase.count('!'))
    elif '?' in frase:
        QtFrases = QtFrases + int(frase.count('?'))
    
    return QtFrases