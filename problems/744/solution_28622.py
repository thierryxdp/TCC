# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    import math
    x = math.floor(len(s) / 2)
    return '#' + s[0:x] + '#' + s[x:len(s)] + '#'