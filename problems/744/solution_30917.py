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