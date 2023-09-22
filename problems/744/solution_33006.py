# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    return '#'+s[:abs(len(s)/2)]+'#'+s[abs(len(s)/2):]+'#'