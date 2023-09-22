# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
Função que receba uma string s, e retorne a mesma string
porém com '#' no início, no meio e no final da mesma.
str -> str
	'''
    tamanho = len(s)
    meio = tamanho//2
    return '#' + s[0:meio] + '#' + s[meio:len(s)] + '#'