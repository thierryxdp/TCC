# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
   	x=(len(s)%2)
	str1=str("#")+s[0:x]+str("#")+s[x:]
    return str1