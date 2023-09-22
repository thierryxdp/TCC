# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Essa função recebe uma string e devolve a mesma porém com
    # no inicio, no fim e no meio da mesma'''
    b = len(s)/2
    return '#' + str(s[0:b]) + '#' + str(s[b:]) + '#'