def uppCons(frase):
    """..."""
    """..."""
    i = 0
    while i < len(frase):
        if frase[i] != 'aeiou':
        	return str.upper(frase[i])
        i = i + 1