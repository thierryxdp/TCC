# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
	'''função que recebe uma string e poem o caractere # no inicio no meio e no fim '''
	'''string -> string '''
	import math
	m=math.floor(len(s)/2)
	return '#'+ s [0:m:] + '#' + s[m::]+'#'