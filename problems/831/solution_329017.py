def lingua_p(palavra):
    ''' Dado como parametro uma palavra, retorna essa 
    mesma palavra traduzida para a lingua do p'''
    palavra_traduzida = palavra.lower()
	for letra in palavra_traduzida:
        if letra in 'AEIOUaeiouáéíóúã':
           	parte_palavra = palavra_traduzida[0:(str.index(palavra_traduzida,letra)]
   	return parte_palavra