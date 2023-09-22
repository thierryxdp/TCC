def lingua_p(palavra):
    ''' '''
    for letra in palavra:
        if letra in 'AEIOUaeiou':
        	letra_nova= 'p' + letra
            indice_letra=palavra.index(letra)
            palavra_nova=palavra[0:indice_letra+1]+letra_nova
	return palavra_nova