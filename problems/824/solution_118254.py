"""
"""
def uppCons(frase):
    i = 0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
        	str.replace(frase, frase[i], str.upper(frase[i]))
    	i = i + 1
    return frase