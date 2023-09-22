# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que, ao receber uma string, ganha 3 no início,meio e fim dela; str -> str'''
    metade = len(s)//2
    return '#' + s[0:metade] + '#' + s[metade:len(s)] + '#'