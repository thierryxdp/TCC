# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
""" retorna uma string com # no inicio, no meio e no final 
	str->str"""
y='#'
return y+s[0:(len(s))//2]+y+s[((len(s))//2):]