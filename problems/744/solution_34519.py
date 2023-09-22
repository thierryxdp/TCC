# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """ recebe uma string e retorna seu valor com o caracter # no inico meio e final da mesma.
    	ex: ab -> #a#b# """
	return '#' + str(s) + len(str(s))