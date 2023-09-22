def uppCons(frase):
    i=0
    letra = 'bcdfghjklmnpqrstvxwyz'
    while letra[i]<len(frase):
          letra[i] = str(frase.upper())
        i=i+1
    return str(frase.upper())