# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import(math)
def hashtag(s):
    x = len(s)//2
    y = math.ceil(x)
    inicio = s[0:x]
    inicioimpar = s[0:x-1]
    final = s[x:len(s)]
    if len(s)!= 0:
        return str('#')+str(inicioimpar)+str('#')+str(final)+str('#')
    else:
    	return str('#')+str(inicio)+str('#')+str(final)+str('#')