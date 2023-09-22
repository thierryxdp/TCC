# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ''' '''
	juncao= '#'+s+'#'
    meio= len(s)//2
    resultado= juncao[:meio] + '#' + juncao[meio:]
    return resultado