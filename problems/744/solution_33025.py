# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    if len(s)%2==0:
        l=len(s)/2
    else:
        l=(len(s)/2)-1       
    return '#'+s[:l]+'#'+s[l:]+'#'