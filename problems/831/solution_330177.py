def linga_p(palavra):
    """Adiciona uma letra p antes da vogal de uma dada palavra.
	 str -> str """
    nova_palavra = '' 	
    vogais = 'aeiou'
    for p in palavra:
        nova_palavra +=p
        if p in vogais:
            nova_palavra += 'p' + p
    return nova_palavra