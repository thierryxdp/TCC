# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Retorna a string # no inicio, no meio e no final
       str->str"""
    if len(s)==4:
        return '#'+s[0:2]+'#'+s[2:]+'#'
    elif len(s)==5:
        return '#'+s[0:2]+'#'+s[2:]+'#'
    elif len(s)==6:
        return '#'+s[0:3]+'#'+s[3:]+'#'
    elif len(s)==7:
        return '#'+s[0:3]+'#'+s[3:]+'#'
    elif len(s)==8:
        return '#'+s[0:3]+'#'+s[5:]+'#'
    elif len(s)==9:
        return '#'+s[0:3]+'#'+s[3:]+'#'
    elif len(s)==10:
        return '#'+s[0:3]+'#'+s[3:]+'#'
    elif len(s)==11:
        return '#'+s[0:3]+'#'+s[3:]+'#'