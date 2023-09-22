# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''dado uma string de entrada são inseridos # no
    inicio,meio e fim da str de entrada'''
    '''str->str'''
    s1=len(s)//2
    return '#'+s[0:s1]+'#'+s[s1:]+'#'