#4.a
#usando map
def uppCons(frase):
    list(frase)
    for letra in frase:
        if letra in [bcdfghjklmnpqrstvwxyzçBCDFGHJKLMNPQRSTVWXYZÇ]:
        	str.upper(letra)
    ''.join(frase)
    return frase