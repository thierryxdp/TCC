# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
from math import floor
def hashtag(s: str) -> str:
    '''
    Retorna frase dada com uma "#" no início, meio e final dela
    '''
    metade = floor(len(s) / 2)
    return '#' + str(s)[:metade] + '#' + str(s)[metade:] + '#'