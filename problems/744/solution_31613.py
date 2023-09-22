# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''retorna a string escolhida mas com # no comeco, no meio e no fim
    param s: str
    return: tuple
    '''
    s= s[:2] + '#' + s[3:]
    return '#' + s + '#'