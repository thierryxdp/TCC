# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    i = round(len(s)/2)
    return '#'+s[:i]+'#'+s[1-i:]+'#'