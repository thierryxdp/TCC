def lingua_p(palavra):
    '''Dada uma palavra, retorna essa mesma
    palavra na lingua do P'''
    i = 0
    for letra in palavra:
        if letra in 'aâãáeéiíoóuú':
            palavra = palavra[i]+ 'p' + letra 
            i += 1
	return palavra