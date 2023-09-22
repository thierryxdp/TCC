# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    import math
    if(len(s)==0):
        return '###'
    else:
        x = len(s)
        s = s[0:(math.floor(x/2))] + '#'+ s[(math.floor(x/2):-1)]+'#'+s[(math.floor(x/2)):-1] + s[-1]
        s = '#' + s
        s = s + '#'
        return s