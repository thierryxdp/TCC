def uppCons(frase):
    contador=0
    letra = 'bcdfghjklmnpqrstvxwyz'
    while letra[contador]<=len(frase):
          letra[contador] = str(frase.upper())
    else:
        return str(frase.upper())