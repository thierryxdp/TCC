# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
from math import*
def hashtag(s):
    """ dado uma string, insere # no inicio meio e fim da strin;
    str -> str"""
    a=int(len(s)/2)
    if a%2 == 0:
        return '#' + s[0:a]+ '#' + s[a:len(s)] + '#'
    else:
        return '#' + s[0:floor(a)]+ '#' + s[floor(a):len(s)] + '#'