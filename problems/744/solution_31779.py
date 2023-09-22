# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Esta e a funcao que recebe uma string e insere nela
    o caractere # no inicio, meio e fim dela
    str -> str'''
    a = '#' + s[:len(s)//2] + '#' + s[len(s)//2:] + '#'
    return a