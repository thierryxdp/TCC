# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
	meio = len(s)//2
	final = len(s)
	return "#" + s[0:meio] + "#" + s[meio:final] + "#"