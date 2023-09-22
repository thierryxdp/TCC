# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    x = len(s)
    if x%2==0:
        return '#'+s[:x//2]+'#'+s[x//2:]+'#'
    elif x%2!=0:
        return '#'+s[:(x-1)//2]+'#'+s[(x-1)//2:]+'#'