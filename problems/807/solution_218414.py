def conta_frases(frase):
    a = (frase.count('?')/frase.count('?'))
    b = (frase.count("...")/frase.count("..."))
    c = (frase.count('!')/frase.count('!'))
    d = (frase.count('.')/frase.count('.'))
    
    return (a+b+c+d)