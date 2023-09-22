# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    i = math.floor( len(s)/2 )
    j = len(s)
    if( len(s)%2 == 0):
        return '#' + s[0:i] + '#' + s[-i:j] + '#'
    elif( len(s) == 1):
        return '#' + s + '#'
    else:
        return '#' + s[0:i] + '#' + s[(-i-1):j] + '#'