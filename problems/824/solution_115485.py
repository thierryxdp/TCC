def uppCons(frase):
    contador=0
    letra = 'bcdfghjklmnpqrstvxwyzç'
    vogal = 'aeiou'
    letra_maius= ' '
    while letra[contador]<len(frase):
          if frase[contador] in letra:
            letra_maius=letra_maius+frase[contador].upper()
            contador=contador+1
    return letra_maius