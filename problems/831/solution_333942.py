def lingua_p(palavra):

	txt = list(palavra)
	vogal = ['a','e','i','o','u']

	for i in range(len(txt)):
		if txt[i] in vogal:
			txt = txt[i] + 'p' + txt[i] 
			Txt[i] = str.replace(txt[i],txt[i],txt)

	return "".join(txt)