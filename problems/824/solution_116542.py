def uppCons (frases):
    i = 0
    aux = ''
    while i < len(frase):
       if frases[i] in `bcdfghjklmnpqrstvxwyz':
       aux += frase[i].upper()
    else:
        aux += frase[i]
    i += 1
    return aux