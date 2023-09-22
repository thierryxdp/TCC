def lingua_p(palavra):
    '''Dada uma palavra, retorna essa mesma
    palavra na lingua do P'''
    for letra in palavra:
        if letra in 'aâãáeéiíoóuú':
            letra = letra + 'p' + letra
	oi = palavra
	return oi