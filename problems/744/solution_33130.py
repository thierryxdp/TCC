# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''funçao que receve uma string e insere o caractere '#' no inicio, meio e fim dela.
    str -> str'''
    mudar = int(len(s)/2)
    mudar2 = len(s)
    return s[:0]+'#'+s[:mudar]+'#'+s[mudar:mudar2]+'#'