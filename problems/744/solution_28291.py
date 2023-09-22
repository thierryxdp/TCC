# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """função que dada uma string, retorna ela com # no inicio, meio e fim; str->str"""
    return '#'+ s[:len(s)//2] + '#' + s[len(s)//2:] +'#'