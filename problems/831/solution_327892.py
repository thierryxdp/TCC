def lingua_p(palavra):
	'''função que dada uma palavra em português retorna esta mesma palavra
    traduzida para a língua do P; str-->str'''
	vogais='AEIOUaeiou'
	for letra in palavra:
		if letra in vogais:
			palavra=str.replace(palavra,letra,letra+'p'+letra)
			vogais=str.replace(vogais,letra,'')
	return str.lower(palavra)