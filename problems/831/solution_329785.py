def lingua_p (palavra):
    for v in palavra:
        if v in 'aeiouAEIOU':
            palavra = str.replace(palavra,v,v+'p'+v,1)
	return palavra