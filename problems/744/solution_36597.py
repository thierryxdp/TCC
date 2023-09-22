# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    r=len(s)//2
    return '#'+s[:r]+'#'+s[r:]+'#'