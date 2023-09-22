# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> stru
def hashtag(s):
    a=sum(s)
    b=a//2 
    return '#'+str(s[0:b])+'#'+str(s[b:])+'#'