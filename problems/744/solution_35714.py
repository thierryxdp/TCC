# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> stru
def hashtag(s):
    l=list(s)
    a=len (l)
    b=a//2 
    return '#'+l[0:b]+'#'+l[b:]+'#'