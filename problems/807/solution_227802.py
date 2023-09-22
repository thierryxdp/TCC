def conta_frases(texto):
    a=len(texto.split('.'))-1-d
    b=len(texto.split('!'))-1
    c=len(texto.split('?'))-1
    d=len(texto.split('...'))-1
    return a+b+c+d