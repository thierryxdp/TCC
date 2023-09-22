def lingua_p(palavra):
    '''Dada uma palavra, retorna essa mesma
    palavra na lingua do P'''
    i = 1
    for letra in palavra:
        if letra in 'aâãáeéiíoóuú':
		palavra = palavra[0:i] + 'p' + letra 
            i += 1
	return palavra