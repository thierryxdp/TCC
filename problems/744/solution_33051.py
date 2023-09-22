# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Retorna uma nova string com # no inicio, no meio e no final da palavra"""
    x = len(s)//2
    return '#' + s[:x] + '#' + s[x:] + '#'