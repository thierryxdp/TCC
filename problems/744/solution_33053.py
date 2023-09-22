# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''retorna o caractere '#' no início, no meio e no final da string
	Entrada: str
	Saída: str'''
    x= len(s)//2
    return '#'+s[:x]+'#'+s[x:]+'#'