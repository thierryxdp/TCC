def uppCons(frases):
    i=0
    aux = ''
    while i < len(frase):
    	if frase[i] in 'bcdfghjklmnpqrstvxwyzç':
        aux += frase[i].upper()
    else:
        aux += frase[i]
    i += 1
    return aux