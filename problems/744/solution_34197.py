# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''funcao que insere uma # em seu inicio, meio e fim
    ass: str->str'''
    x=len(s)//2
	return '#'+s[0:x]+'#'+s[x:]+'#'