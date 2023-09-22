def lingua_p (palavra):
    for v in palavra:
        if v == 'aeiouAEIOU':
            palavra = str.replace(palavra,v,'p'+v,1)
	return palavra