# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que retorna uma string com um # no incio, no meio e no fim'''
    '''str -> str'''
    k = len(s) // 2
    return '#' + s[:k] + '#' + s[k:] + '#'