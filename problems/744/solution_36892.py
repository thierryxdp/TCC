# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que recebe uma string e insere # no inicio, no meio e no fim dessa string.
    str -> str'''
    if len(s)%2==0:
        pausa = len(s)//2
    else:
        pausa = (len(s)-1)//2
    return '#' + s[:pausa] + '#' + s[pausa:] + '#'