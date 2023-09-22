# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(S):
    '''retorna uma string com # no inicio meio e fim dela
str->str'''
    y='#'
    return y+S[0:(len(S))//2]+y+S[((len(S))//2)+2:]+y