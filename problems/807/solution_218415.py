def conta_frases(frase):
    a = (frase.count('?'))
    b = (frase.count("..."))
    c = (frase.count('!'))
    d = (frase.count('.'))
    
    if b >= 1:
        return ((a+1+c+d)-3)
    
    else:
        return (a+b+c+d)