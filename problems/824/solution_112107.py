#4.a
#usando map
def uppCons(frase):
    frase2 = list(frase)
    for letra in range(len(frase2)):
        if frase2[letra] in ['bcdfghjklmnpqrstvwxyz']:
        	frase2[letra] = str.upper(letra)
    ''.join(frase2)
    return frase2