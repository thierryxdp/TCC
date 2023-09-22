"""
"""
def uppCons(frase):
    i = 0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
    	i += 1
        	fraseup = str.replace(frase, frase[i], str.upper(frase[i]))
    return fraseup