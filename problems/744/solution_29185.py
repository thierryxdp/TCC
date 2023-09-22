# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''str -> str'''
    x=int(len(s[:])/2)
    if len(s)%2==0:
        return '#'+str(s[:x])+'#'+str(s[x:])+'#'
    else:
        return '#'+str(s[:x])+'#'+str(s[x:])+'#'