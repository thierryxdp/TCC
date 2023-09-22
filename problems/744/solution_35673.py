# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''coloca # no inicio meio e fim do texto fornecido'''
    '''str -> str'''
    t = len(s)//2
    h = '#'
    return h + s[:t] + h + s[t:] + h