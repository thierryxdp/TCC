# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    metade=s[0:2]
    final=s[2:]
    return '#'+metade[0:2]+'#'+final[2:]+'#'