# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    n=len(s)
    return '#'+s[0:n//2]+'#'+s[n//2+1:30]+'#'