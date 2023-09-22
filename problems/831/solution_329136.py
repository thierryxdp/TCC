def lingua_p(palavra):
    new = [n+'p'+n for n in palavra if n in 'aeiou']
    fo = palavra
    for n in fo:
        if n in 'aeiou':
            n = n+'p'+n
        else:
            n = n
    	return fo