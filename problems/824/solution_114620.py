def uppCons(frase):
    contador=0
    letra = 'bcdfghjklmnpqrstvxwyz'
    while letra[contador]<=len(frase):
          letra[contador] = str(frase.upper())
        i=letra[contador]+1
    else:
        return str(frase.upper())