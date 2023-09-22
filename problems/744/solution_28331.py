# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Recebe uma string e insere o caractere '#' no início, meio e fim dela.
    str ---> str'''
    import math
    indice_do_meio = math.floor(len(s)/2)
    return '#' + s[0:indice_do_meio] + '#' + s[math.floor(len(s)/2):] +'#'