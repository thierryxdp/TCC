# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    meio=int((len(s)-1)/2)
    if (len(s)%2==0) and (len(s)!=1):
        return '#'+s[0:meio+1]+'#'+s[meio+1:]+'#'
    elif (len(s)%2!=0) and (len(s)!=1):
        return '#'+s[0:meio]+'#'+s[meio:]+'#'
    else:
        return '##'+s+'#'