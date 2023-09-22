# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
   	return '#'+str.partition(s,(len(s)/2)) + '#'