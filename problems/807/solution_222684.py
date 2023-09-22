def conta_frases(frase):
    f= 0
    frase = str.split(frase)
    if frase =="." or frase == "!" or frase == "?" or frase =="...":
         return f = f+1
    else:
        return f