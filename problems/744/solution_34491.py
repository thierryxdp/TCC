# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
  
	x = len(s)
	y = s[:x // 2]
	z = s[x // 2:]
	r = '#' + y + '#' + z + '#'
	return r