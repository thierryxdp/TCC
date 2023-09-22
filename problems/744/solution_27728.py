# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
from math import floor
def hashtag(s: str) -> str:
    '''Retorna o símbolo # no início, meio e fim da string s.'''
    comp_da_string = len(s)
    if len(s)%2==0:
        metade_da_string = int(len(s)/2)
        return '#' + s[0:metade_da_string] + '#' + s[metade_da_string:comp_da_string] + '#'
    else:
        metade_da_string = int(floor(len(s)/2))
        return '#' + s[0:metade_da_string] + '#' + s[metade_da_string:comp_da_string] + '#'