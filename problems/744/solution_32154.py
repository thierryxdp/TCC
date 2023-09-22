# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    '''
    a = int(len(str(s))//2)
    palavraf = '#'+s[0:a]+'#'+[(a+1)::]+'#'
    return palavraf