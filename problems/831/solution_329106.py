def lingua_p(palavra):
	'''Dado como parametro uma palavra, retorna a mesma
	traduzida para a lingua do P'''
    palavra1 = palavra.lower()
    i = 1
    contador = 0
    for letra in palavra1:
        if letra in 'aeiou':
      		palavra1 = palavra1[0:i+contador] + 'p' + letra
        	contador += 2
		i += 1
    return palavra1