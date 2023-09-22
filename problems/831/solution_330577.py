def lingua_p(palavra):
    '''calcule uma funcao que receba como entrada uma palavra e retorne
    esta mesma palavra traduzida para a lingua do P, isto é, inserindo a 
    letra 'p' após cada vogal da palavra. str-->str.'''
	palavra = str.lower(palavra)
	linguaP = ''
	for i in palavra:
		if i in 'aeiouáâãéêóôú':
			linguaP = linguaP + i + 'p' + i
		if i not in 'aeiouáâãéêóôú':
			linguaP = linguaP + i
	return linguaP