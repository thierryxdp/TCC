def conta_frases(frase):
    ''''''
    F = ()
    if frase == '...':
        F = str.count(frase,'...')
    if frase == '!':
        F = str.count(frase,'!') 
    if frase == '.':
        F = str.count(frase,'.')
    if frase == '?':
        F = str.count(frase,'?')
    return F