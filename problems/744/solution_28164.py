# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    nova_s= len(s)//2
    return '#'+s[0:nova_s]+'#'s[nova_s]+'#'