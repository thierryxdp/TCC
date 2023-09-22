# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que insere uma hashtag no início, no meio e no final de uma string s;
    str -> str'''
    x = int(len(s)/2)
    if len(s) % 2 == 0:
    	return '#'+s[:x]+'#'+s[x:]+'#'
	elif len (s) % 2 != 0:
        return '#'+s[:x]+'#'+s[x+1:]+'#'