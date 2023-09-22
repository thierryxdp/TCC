def lingua_p(palavra):
    '''Dada uma palavra, retorna essa mesma
    palavra na lingua do P'''
    palavra_traduzida = palavra(::)
    palavra_traduzida.lower()
    for letra in palavra_traduzida:
        if letra in 'aâãáeéiíoóuú':
            letra = letra + 'p' + letra
	return palavra_traduzida