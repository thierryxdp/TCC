# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    abcd= s[0:s]
    abcde= s[0:s]
    has1= '#'+s[0:1]+'#'+s[2:3]+'#'
    has2= '#'+s[0:1]+'#'+s[2:4]+'#'
    if s==abcd:
        return has1
    elif s==abcde:
        return has2