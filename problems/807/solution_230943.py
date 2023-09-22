def conta_frases(texto):
    a = [texto.split('. ')]
    b = [texto.split('! ')]
    c = [texto.split('... ')]
    d = [texto.split('? ')]
    x = a+b+c+d
    return x