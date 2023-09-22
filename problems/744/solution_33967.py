# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    if len(s)%2 == 0:
        m = int(len(s)/2)
        return '#'+s[0:m]+'#'+s[m:]+'#'
    else:
        m = int((len(s)-1)/2)
        return '#'+s[0:m]+'#'+s[m:]+'#'