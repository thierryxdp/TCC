# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''recebe uma string e retorna a mesma str com um # no inicio,
    um no meio e um no final
    str -> str'''

    meio = round(len(s)/2)

    return '#' + s[0:meio] + '#' + s[meio:len(s)] +'#'