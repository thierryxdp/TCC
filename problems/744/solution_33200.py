# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Essa função recebe uma string e devolve a mesma porém com
    # no inicio, no fim e no meio da mesma'''
    string = 's'
    return '#' + 's[0:len(s)/2]' + '#' + 's[Len(s)/2:]' + '#'