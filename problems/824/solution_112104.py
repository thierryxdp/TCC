#4.a
#usando map
def uppCons(frase):
    list(frase)
    for letra in range(len(frase)):
        if frase[letra] in ['bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ']:
        	frase[letra] = str.upper(letra)
    ''.join(frase)
    return frase