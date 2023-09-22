# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ''' dada a palavra s retorna a palavra com # no começo, meio e fim
    str->str'''
    return '#' + s[:(len(s)//2)] + '#' + s[(len(s)//2):] + '#'