# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Retorna a string(s) com hashtags no inicio, no meio e no fim dela
    str -> str'''
    half = len(s) // 2
    a = s[0:half]
    b = s[half:]
    return '#' + a + '#' + b + '#'