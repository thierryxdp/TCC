# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    x = len(s)
    y = x%2
    inicio = s[0:x//2]
    fim = s[(x//2):x]
    if y != 0:
    	return str('#')+inicio+str('#')+fim+str('#')
    else:
        return str('#')+inicio+str('#')+fim+str('#')