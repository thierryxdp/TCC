# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
from math import floor

def hashtag(s):
    """..."""
    meio = floor((len(s))/2)
    return '#'+ s[0:meio]+'#'+s[meio:]