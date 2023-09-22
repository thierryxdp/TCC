def conta_frases(texto):
    a = [texto.split('. ')]
    if '. ' in texto == False:
        len(a) = 0
    b = [texto.split('! ')]
    if '! ' in texto == False: 
        len(b) = 0
    c = [texto.split('... ')]
    d = [texto.split('? ')]
    x = len(a)+len(b)+len(c)+len(d)
    return x