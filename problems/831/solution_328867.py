def lingua_p(palavra):
    '''Dada uma palavra, retorna essa mesma
    palavra na lingua do P'''
    i = 0
    for letra in palavra:
        if letra in 'aâãáeéiíoóuú':
        	letra = letra + 'p' + letra
            palavra = palavra + letra
	return palavra