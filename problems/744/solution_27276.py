# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
   """Função que insere o caractere "#" no inicio, meio e final da string. str -> str."""
	return "#" + str (s)[0: len(s)//2] + "#" + str (s) [len (s)//2 :] + "#"