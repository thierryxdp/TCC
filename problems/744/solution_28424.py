# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    a=len(s)
    b=a/2
    c=round(b-0.5)
    if(a%2) == 0:
    	return "#" + s[0:int(c)] + "#" + s[int(c):] +"#"
	else:
        return "#" + s[0:int(c+1)] + "#" + s[int(c+1):] +"#"