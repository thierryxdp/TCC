# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
from math import floor
def hashtag(s):
    '''Dada uma string s, retorna s com # no início, meio e fim; str -> str'''
    MeioS=floor(len(s)/2)
    return '#' + s[:MeioS] + '#' + s[MeioS:] + '#'