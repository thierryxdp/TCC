# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que introduz '#' no inicio, no meio, e no final da string'''
    i=(len(s)//2)
    return '#' + s[:i] + '#' + s[i:] + '#'