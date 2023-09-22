def conta_frases(frase):
    QtFrases = 0
    
    if '. ' in frase:
        QtFrases = QtFrases + int(frase.count('. '))
    if '...' in frase:
        frase.replace('...','+')
    if '+' in frase:
        QtFrases = QtFrases + (frase.count('+'))
    if '!' in frase:
        QtFrases = QtFrases + int(frase.count('!'))
    if '?' in frase:
        QtFrases = QtFrases + int(frase.count('?'))
    
    return QtFrases