def uppCons(frase):
    i = 0
    newfrase = frase
    while i < len(frase):
        if frase[i] == 'bcdfghjklmnpqrstvwxyz':
			str.upper(frase[i])
        i+=1
    return frase