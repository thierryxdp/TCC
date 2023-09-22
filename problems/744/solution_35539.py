# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    if(len(s)%2==0):
    	return '#'+s[0:3]+'#'+s[3:-1]+s[-1]+'#'
    elif(len(s)%2==1):
    	return '#'+s[0:4]+'#'+s[4:-1]+s[-1]+'#'