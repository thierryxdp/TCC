# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
	"""Esta funcao recebe uma string s, e a retorna com '#' no inicio, meio e
	no final."""
	if len(s)%2==0:
        metade=int(len(s)/2)
		return '#'+s[0:metade]+'#'+s[metade+1::]+'#'