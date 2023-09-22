# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ''' função que recebe uma str e insira um caractere no inicio, no meio e no final dela
    str, str '''
    len(s)
    return '#' + s[0:len(s)//2] + '#' + s[len(s)//2 +2:] + '#'