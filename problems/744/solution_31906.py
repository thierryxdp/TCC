# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Insere hashtags na string fornecida'''
    k = len(s)//2
    a1 = s[0:k]
    a2 = s[k:]
    return '#' + a1 + '#' + a2 + '#'