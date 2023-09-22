# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    return '#'+s.replace(s[(len(s))/2],'#')+'#'