# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    x = len(s)
    y = x%2
    inicio = s[0:x//2]
    inicioimpar = s[0:(x//2)-1]
    fim = s[(x//2):x]
    fimimpar = s[(x//2)-1:x]
    if y != 0:
    	return str('#')+inicio+str('#')+fim+str('#')
    else:
        return str('#')+inicio+str('#')+fim+str('#')