# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag (s):
    if len (s) == 1:
        return '#'+s[0]+'#'+s[1]+'#'
    elif len (s) == 2:
        return '#'+s[:1]+'#'+s[1:]+'#'
    elif len (s) == 3:
        return '#'+s[:1]+'#'+s[1:]+'#'
    elif len (s) == 4:
        return '#'+s[:2]+'#'+s[2:]+'#'
    elif len (s) == 5:
        return '#'+s[:2]+'#'+s[2:]+'#'
    elif len (s) == 6:
        return '#'+s[:3]+'#'+s[:]+'#'
    elif len (s) == 7:
        return '#'+s[:3]+'#'+s[3:]+'#'
    elif len (s) == 8:
        return '#'+s[:4]+'#'+s[4:]+'#'
    elif len (s) == 9:
        return '#'+s[:4]+'#'+s[4:]+'#'
    elif len (s) == 10:
        return '#'+s[:5]+'#'+s[5:]+'#'
    elif len (s) == 11:
        return '#'+s[:5]+'#'+s[5:]+'#'
    elif len (s) == 12:
        return '#'+s[:6]+'#'+s[6:]+'#'
    elif len (s) == 13:
        return '#'+s[:6]+'#'+s[6:]+'#'