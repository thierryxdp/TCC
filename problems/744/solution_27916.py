# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que insere # no início, meio e final de uma dada string'''
    import math
    spam = math.floor(len(s)/2)
    return '#' + s[:spam] + '#' + s[spam:] + '#'