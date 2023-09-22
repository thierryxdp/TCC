# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    a= [0]
    ab= s[0:1]
    abc= s[0:2]
    abcd= s[0:3]
    abcde= s[0:4]
    abcdef= s[0:5]
    abcdefg= s[0:6]
    abcdefgh= s[0:7]
    abcdefghi= s[0:8]
    abcdefghij= s[0:9]
    has1= '#'+'#'+s[0]+'#'
    has2= '#'+s[0]+'#'+s[1]+'#'
    has3= '#'+s[0:1]+'#'s[2]+'#'
    has4= '#'+s[0:1]+'#'+s[2:3]+'#'
    has5= '#'+s[0:1]+'#'+s[2:4]+'#'
    if s==s[0]:
        return has1
    elif s==s[0:1]:
        return has2