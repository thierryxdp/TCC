def lingua_p(palavra):

	n_palavra = ''

	i = 0
	while i<len(palavra):
		n_palavra += str(palavra[i] + 'p' + palavra[i]) if palavra[i] in 'aeiouáéíóúâ' else palavra[i]
		i += 1

	return n_palavra