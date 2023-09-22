# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Recebe uma string como entrada e insere o caractere # no ínicio, meio e fim dessa string.'''
    meio = len(s)//2
    metade_1 = s[0:meio]
    metade_2 = s[meio:]
    return '#' + metade_1 + '#' + metade_2+'#'