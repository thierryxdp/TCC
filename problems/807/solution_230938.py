def conta_frases(texto):
    a = [texto.split('. ')]
    b = [texto.split('! ')]
    c = [texto.split('... ')]
    d = [texto.split('? ')]
    x = len(a)*1+len(b)*1+len(c)*1+len(d)*1
    return x