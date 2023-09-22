def uppCons (frase):
    i = 0
    aux = ''
    while i < len(frase):
       if frases[i] in 'bcdfghjklmnpqrstvxwyzÇ':
           aux += frase[i].upper()
    else:
        aux += frase[i]
    i += 1
    return aux