# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    equacao1=len(s)/2

	v1='#'+s[:(int(equacao1))]+'#'+s[int(equacao1):]+'#'

	return v1