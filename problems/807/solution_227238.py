def conta_frases(frases):
    frase=0
    if '.' in frases:
     frase+=(str.count(frases,'.'))
    if '!' in frases:
     frase+=(str.count(frases,'!'))
    if '?' in frases:
     frase+=(str.count(frases,'?'))
    if '...' in frases:
     frase+=(str.count(frases,'...'))-4
     return frase
    else:
        return frase