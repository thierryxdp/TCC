# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Dada uma string, s, insere o caractere "#" no início,
    no meio e no final dela.
    str -> str'''
    x=len(s)//2
	return '#'+s[0:x]+'#'+[x:]+'#'