def conta_frases(frase):
    a = frase
    x = str.split('.',str.split('!',str.split('?',str.split('...',a))))
    y = str.join('#',(x))
    return y.count('#')