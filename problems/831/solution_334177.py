def lingua_p(palavra):
	traducao=''
	i=0
	while i in range(len(palavra)):
		if palavra[i] in "aeiouAEIOUáéíóú":
			traducao = traducao + palavra[i] + 'p' + palavra[i]
			i += 1
		else:
			if palavra[i] not in "aeiouAEIOU":
				traducao = traducao + palavra[i]
				i += 1
	return str.lower(traducao)