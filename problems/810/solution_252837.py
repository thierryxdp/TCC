def inverte(frase):
    """ Função que recebe um argumento em forma de frase e retorna, com as mesmas palavras, uma frase invertida"""
    frasesSpontuacao = frase
    minFrase = str.lower(frasesSpontuacao)
    part = str.split(minFrase, " ")
    list.reverse(part)
    reverseStr = ' '
    for k in part:
    	reverseSTR += ' ' + k
	return reverseSTR