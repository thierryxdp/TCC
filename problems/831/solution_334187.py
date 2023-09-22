def lingua_p(palavra):
    for e in palavra:
        if e in 'aeiou':
            e=e+'p'
    	return palavra