def conta_frases(texto):
    a=len(texto.split('...'))-1
    b=len(texto.split('!'))-1
    c=len(texto.split('?'))-1
    d=len(texto.split('.'))-1-(a*3)
    
    return a+b+c+d