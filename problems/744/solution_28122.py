# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que substitui as posições por #
    str-> str'''
    n = (len(s)//2)
    return '#' +s[0:n]+'#'+s[n:]+'#'