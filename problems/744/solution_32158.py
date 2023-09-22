# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    '''
    a = int(len(str(s))//2)
    palavraf = '#'+str(s[0:a])+'#'+str(s[(a)::])+'#'
    return palavraf