# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    if len(s)%2==0:
        return '#'+s[0:int(len(s)/2)]+'#'+s[int(len(s)/2):]+'#'
    else:
        return '#'+s[0:int((len(s)-1)/2)]+'#'+s[int((len(s)-1)/2):]+'#'