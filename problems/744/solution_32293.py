# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    i = int(len(s)/2)
    if i==int:
        return '#'+s[:i]+'#'+s[i:]+'#'
    elif i==float:
        return '#'+s[:i-1]+'#'+s[1+i:]+'#'