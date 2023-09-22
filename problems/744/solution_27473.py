# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''recebe uma string e retorna a mesma com 3 #, no inicio, no final e no meio, respectivamente.
    str -> str'''
    meio = len(s)//2
    return '#' + s[0:metade] + '#' + s[metade:len(s)] + '#'