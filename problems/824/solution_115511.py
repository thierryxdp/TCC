def uppCons(frase):
    contador=0
    letra ='bcdfghjklmnpqrstvxwyzç'
    letra_maius=' '
    while letra[contador]<len(frase):
        if frase[contador] in letra:
            letra_maius=letra_maius+frase[contador].upper()
        else:
            letra_maius=letra_maius+frase[contador]
    contador=contador+1
    return letra_maius