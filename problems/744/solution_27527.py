# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Com uma string de entrada retorna a mesma string com # no inicio, meio e no final
    str->str"""
    d=(len(s)//2)
    return '#' + s[:d] +'#' + s[d:] + '#'