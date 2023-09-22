# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''funcao que insere uma hashtag no inicio meio e fim da str s; str->str'''
    import math
    x=(math.floor(len/2))
    subs1=s[0:x]
    subs2=s[(x+1):]
    return '#'+str(subs1)+'#'+str(subs2)+'#'