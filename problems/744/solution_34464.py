# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ''' Essa função recebe hashtag no inicio meio e fim; str->str'''
    return '#' +[:len(s)//2]+'#' +s[len//2:]+'#'