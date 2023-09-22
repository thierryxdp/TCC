def conta_frases(frases):
    frase=0
    if '.' in frases:
     frase+=(len(str.split(frases,'.')))-1
    if '!' in frases:
     frase+=(len(str.split(frases,'!')))-1
    if '?' in frases:
     frase+=(len(str.split(frases,'?')))-1
    if '...' in frases:
     frase+=(len(str.split(frases,'...')))-4
    return frase
     else:
    return frase