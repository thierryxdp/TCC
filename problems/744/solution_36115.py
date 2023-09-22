# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
	s1 = s[:len(s)//2]
	s2 = s[len(s)//2:]
	h = str('#')
    return h+s1+h+s2+h