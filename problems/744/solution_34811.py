# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
from math import floor 
def hashtag(s):
    '''recebe uma string s e retorna essa mesma string com o caractere # no inicio,meio e fim
    str -> str'''
    quant=floor(len(s)/2)
    subst1=s[0:quant]
    subst2=s[quant:]
    return str('#') + str(subst1) + str('#') +str(subst2) + str('#')