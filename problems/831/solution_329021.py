def lingua_p(palavra):
    ''' Dado como parametro uma palavra, retorna essa 
    mesma palavra traduzida para a lingua do p'''
    palavra_traduzida = palavra.lower()
    i = 0
	for letra in palavra_traduzida:
        if letra in 'AEIOUaeiouáéíóúã':
 			palavra_traduzida = palavra_traduzida[0:i] + letra + 'p' + letra + palavra_traduzida[i+1::] 
    	i += 1
	return palavra_traduzida