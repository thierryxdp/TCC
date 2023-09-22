def conta_frases(frase):
    a = (frase.count('?'))
    b = (frase.count("..."))
    c = (frase.count('!'))
    d = (frase.count('.'))
    
    if (b + d) >= 4:
        return int((a+b+c+d+e)-3)
    
    elif d >= 1:
        return(a+b+c+1+e)

    else:
        return(a+b+c+d)