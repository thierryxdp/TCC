# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
	""" Esta função concatena # no inicio,meio e fim da string s
	str -> str """

	x = len (s)//2
	
	return '#' + s[:x] + '#' + s[x:] + '#'