# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    '''
    	Coloca a hashtag no ínicio, no meio e no final da string.
		Parâmetro 1: string
        Resultado: string
	'''
	x = math.floor(len(s) / 2)
    nova_string = '#' + s[:x] + '#' + s[x:] + '#'
    return nova_string