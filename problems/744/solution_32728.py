# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    x = len(s)//2
    y = x - 1
    z = len(s) % 2
    inicio = s[0:x]
    inicioimpar = s[0:y]
    final = s[x+1:len(s)]
    if not z % 2 == 0 
        return return str('#')+str(inicioimpar)+str('#')+str(final)+str('#')
    else:
    	return str('#')+str(inicio)+str('#')+str(final)+str('#')