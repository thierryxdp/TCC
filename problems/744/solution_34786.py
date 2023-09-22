# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str 
def hashtag(s):
    tam=((len(s))/2)
    if len(s)%2==0:
    	return "#" + s[:((tam)+1)] + "#" + s[((tam)+1):] + "#"
	else:
        return "#" + s[:(tam)] + "#" + s[(tam):] + "#"