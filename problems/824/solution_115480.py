def uppCons(frase):
    contador=0
    letra = 'bcdfghjklmnpqrstvxwyz'
    vogal = 'aeiou'
    letra_maius= ' '
    while letra[contador]<len(frase):
          if frase[contador] in letra:
            letra_maius=letra_maius+frase[contador].upper()
            contador=contador+1
            elif frase[contador] in vogal