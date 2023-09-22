# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def divideString(s):
    '''Dada uma string, s, calcula o número de termos e
    divide por 2.
    str -> int'''
    return len(s)//2
def hashtag(s):
    '''Dada uma string, s, insere o caractere "#" no início,
    no meio e no final dela.
    str -> str'''
	return '#'+s[0:divideString(s)]+'#'+[(divideString(s)+1):]+'#'