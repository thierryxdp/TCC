# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s:str)->str:
    '''Colocar entre '' para colocar hashtags'''
    metade=round(len(s)/2-0.4)
    return '#'+s[:metade]+'#'+s[metade:]+'#'