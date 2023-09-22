def conta_frases(frase):
    ''''''
    F = str.count()
    if frase == '...':
        F = str.count(frase,'...')
    if frase == '!':
        F = str.count(frase,'!') 
    if frase == '.':
        F = str.count(frase,'.')
    if frase == '?':
        F = str.count(frase,'?')
    return F