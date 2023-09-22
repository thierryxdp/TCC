def conta_frases(frase):
    f= 0
    frase = str.split(frase)
    if frase[:] == "." or frase[:] == "!" or frase[:] == "?" or frase[:] =="...":
         ft = f + 1
        return ft
    else:
        return ft