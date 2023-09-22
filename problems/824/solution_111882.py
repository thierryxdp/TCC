def uppCons(frase):
    """..."""
    """..."""
    i = 0
    while i < len(frase):
        if frase[i] != 'aeiou':
        	return str.upper(frase[i]) in frase
        i = i + 1