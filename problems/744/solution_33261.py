# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    A M A N D A --> LEN = 6
    #
    '''
    if len(s)%2==0:
        return '#'+s[0:(len(s)/2)]+'#'