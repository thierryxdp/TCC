# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """ calcula hashtag '#' no inicio meio e final das string"""
    	return "#" + s[ :len(s)//2]+ "#" + s[len(x)//2:len(x)] + "#"