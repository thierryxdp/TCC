# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Essa função recebe uma string e devolve a mesma com #
    no inicio,no fim e no meio da string'''
    return '#' + s[0:len(s)//2] + '#' + s[(len(s)//2:]+ '#'