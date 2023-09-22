# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    x=len(s)
    # essa função taca 3 hashtags na string
    if x%2==0:
    	return str('#') + s[0:round((x/2))] + str('#')+s[round((x/2)):]+str('#')
    else:
    
    	return str('#') + s[0:round((x/2))] + str('#')+s[round((x/2)-0.5):]+str('#')