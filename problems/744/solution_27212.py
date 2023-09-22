# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
from math import floor
def hashtag(s):
    """essa funcao dada uma string s insere uma hashtag no inicio, meio e fim dela
    str -> str"""
     metade = floor(len(s) / 2)
    return '#' + s[0:metade] + '#' + s[metade:] + '#'