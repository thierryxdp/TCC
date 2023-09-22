def conta_frases(frase):
    a=frase.count('?')
    b=frase.count('!')
    c=frase.count('.')
    d=frase.count('...')
    if d=1:
        e=-2
    elif d=2:
        e=-4
    else:
        e=0
    h=a+b+c+e    
    return h