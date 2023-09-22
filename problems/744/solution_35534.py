# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    i=s.split()
    return '#'+s[0:3]+'#'+s[i]+s[-1]+'#'