# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """
    parametro s: é uma string
    me retorna uma uma str que tem # no inicio, meio e fim"""
    s = "#" + s[ : len(s)//] + "#" + s[len(s)//2 : ]
    return s