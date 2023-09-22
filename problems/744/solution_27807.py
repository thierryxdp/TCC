# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Escreva uma funcao que receba uma string e insira o caractere # no inicio, no meio
e no final dela.
    str -> str'''
	i=len(s)
	return '#' + s[0:i//2] + '#' + s[i//2:] + '#'