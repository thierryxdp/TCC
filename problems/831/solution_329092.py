def lingua_p(palavra):
	'''Dado como parametro uma palavra, retorna a mesma
	traduzida para a lingua do P'''
    palavra1 = palavra.lower()
    for letra in palavra1:
        if letra in 'aeiou':
            letra = letra + 'p' + letra
	return palavra1