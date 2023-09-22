# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    j=int(len(s)/2)
    subA=s[0:j]
    subB=s[j:]
    return '#'+subA+'#'+subB+'#'