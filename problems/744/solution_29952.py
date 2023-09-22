# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
	"""a função recebe uma string e coloca o caracter "#" no começo, meio e fim dela; Str -> str"""
	a = len (s)/2
    if a == 0:
		return '#' + s[0:a] + '#' + s[a:] + '#'
	else:
		return '#' + s[0:a] + '#' + s[a:] + '#'