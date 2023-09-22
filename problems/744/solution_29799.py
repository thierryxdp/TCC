# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s:str)->str:
    '''Colocar entre '' para colocar hashtags'''
    return '#'+s[-4:4]+'#'+s[4:-4]+'#'