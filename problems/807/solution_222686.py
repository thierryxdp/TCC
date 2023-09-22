def conta_frases(frase):
    f= 0
    frase = str.split(frase)
    if frase =="." or frase == "!" or frase == "?" or frase =="...":
         f = f+1
        return f
    else:
        return f