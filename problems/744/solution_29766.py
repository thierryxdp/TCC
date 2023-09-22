# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s:str)->str:
    '''Colocar entre '' para colocar hashtags'''
    return '#'+s[:(s/2)]+'#'+s[(s/2):]+'#'