# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    return '#'+str(s)[:str(s)/2]+'#'+str(s)[str(s)/2:]+'#'