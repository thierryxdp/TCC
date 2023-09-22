def conta_frases(frase):
    a = (frase.count('?'))
    b = (frase.count("..."))
    c = (frase.count('!'))
    d = (frase.count('.'))
    
    if (b + d) >= 4:
        return int((a+b+c+d)-3)
    else:
        return(a+b+c+d)