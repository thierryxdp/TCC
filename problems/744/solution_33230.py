# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    p= list(s)
    x = len(p)
    if x%2==0:
        return '#'+s[:x/2]+'#'+s[x/2:]+'#'
    #else:
        #return '#'+s[:(x-1)/2]+'#'+s[(x-1)/2:]+'#'