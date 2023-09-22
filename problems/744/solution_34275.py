# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    '''essa funcao coloca um # no inicio, meio e fim 
    da string'''
    '''str -> str'''
    if (len(s)%2 == 0):
        i2 = ((len(s)/2))
        return '#' + s[1:i2] + '#' + s[i2+1:-1]
    elif (len(s)%2 != 0):
        i2 = math.ceil((len(s)/2))
        return '#' + s[1:i2] + '#' + s[i2+1:-1]