# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    import math
def hashtag(s):
    """Função que coloca # no inicio, meio e fim
    de uma string
     str-> str"""
    meio =math.floor(len(s)/2)
    return '#' + s[:meio] + '#' + s[meio:] +'#'