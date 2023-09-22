# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    w=len(s)//2
    return '#'+s[:w]+'#'+s[w:]+'#'