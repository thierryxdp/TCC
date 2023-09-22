# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):def hashtag(s):
    """ coloca # no inicio, no meio e no final da palavra."""
	l = int(len(s))
    mid = int(l/2)
    return '#'+s[0:mid]+'#'+s[mid:l] +'#'