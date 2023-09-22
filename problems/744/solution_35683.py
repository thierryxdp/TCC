# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    if s%2==0:
        return '#'+s[0:2]+'#'+s[2:]+'#'
    if not(s%2==0):
        return '#'+s[0:2]+'#'+s[2:]+'#'