# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
	i = s/2 - len(s)%2
	s1 = [:i]
	s2 = [i+1:]
	return "#"+s1+"#"+s2+"#"