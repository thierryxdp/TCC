# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    n = len(s)//2 
	x = '#' + s[:n] + '#' + s[n:] + '#'
    return x