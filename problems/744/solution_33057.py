# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que retorna uma string com hashtag no início, no meio e no fim;str->str'''
     i=len(s)/2
     return '#'+s[0:i]+'#'+s[i: ]+'#'