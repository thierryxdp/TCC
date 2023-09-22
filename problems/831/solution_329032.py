def lingua_p(palavra):
    ''' Dado como parametro uma palavra, retorna essa 
    mesma palavra traduzida para a lingua do p'''
    palavra_traduzida = palavra.lower()
    i = 0
	for letra in palavra_traduzida:
        if letra in 'AEIOUaeiouáéíóúã':
 			palavra_traduzida[i:1] = 'p' + letra 
    	i += 1
	return palavra_traduzida