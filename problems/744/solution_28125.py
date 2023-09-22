# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    '''insere o caractere # no início, no meio e no fim  de uma string
    string-> string'''
    quantidade= len(s)
    i = math.ceil(quantidade /2)
    inicio = s[:-i]
    fim = s[-i:]
    frase = '#' + inicio + '#' + fim + '#'
    return frase