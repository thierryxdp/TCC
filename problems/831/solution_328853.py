def lingua_p(palavra):
    '''Dada uma palavra, retorna essa mesma
    palavra na lingua do P'''
	traducao = palavra[::]
    for letra in traducao:
        if letra in 'aâãáeéiíoóuú':
            letra = letra + 'p' + letra
	oi = traducao
	return oi