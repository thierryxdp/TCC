def conta_frases(frase):
    p1 = frase.count('?')
    p2 = frase.count('!')
    p3 = frase.count('.')
    p4= '...'
    if '...' in frase:
        return p1 + p2 + p3 + p4
    elif (p4 + p4) in frase:
        return (p1 + p2 + p3 + p4)-2
    else:
        return p1 + p2 + p3