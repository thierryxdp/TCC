def lingua_p(palavra):
    '''Dada uma palavra, retorna essa mesma
    palavra na lingua do P'''
    palavra.lower()
    for letra in palavra:
        if letra in 'aâãáeéiíoóuú':
            letra = letra + p + letra
	return palavra