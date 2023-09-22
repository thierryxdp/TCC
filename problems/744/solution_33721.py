# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    if len(s) == 4:
        return '#'+s[:2]+'#'+s[2:]+'#'