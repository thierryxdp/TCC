# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que insere hashtag em 3 posições de uma string dada'''
    i = len(s)%2
    x = s[:i]
    y = s[i+1:]
    return '#' + x + '#' + y + '#'