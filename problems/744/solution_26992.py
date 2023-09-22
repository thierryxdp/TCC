# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''funcao que adiciona uma # no inicio, no meio e no final de uma string
    str->str'''
    x=int(floor(len(s)/2))
    y=int(ceil(len(s)/2))
    a=s[0:x]
    b=s[0:y]
    return '#'+a+'#'+b+'#'