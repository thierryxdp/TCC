def lingua_p(palavra):
	'''Dado como parametro uma palavra, retorna a mesma
	traduzida para a lingua do P'''
    palavra1 = palavra.lower()
    i = 0
    for letra in palavra1:
        if letra in 'aeiou':
      		palavra1 = palavra1[0:i+1] + 'p' + letra
		i += 1
	palavra_traduzida = palavra1[::]
    return palavra_traduzida