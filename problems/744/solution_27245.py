# Insere o caractere # no início, meio e fim da string
# s: string
# str-> str
from math import floor
def hashtag(s):
    """Insere o caractere '#' no início, meio e fim de uma string s"""
    q = len(s)/2
    return '#'+s[0:floor(q)]+'#'+s[floor(q):]+'#'