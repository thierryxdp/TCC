# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    import math
    z = len(s)
    y = z/2
    x = y - 0.1
    w = round(x)
    return str('#') + str(s[0:w]) + str('#') + str(s) + str(s[w:]) + str('#')