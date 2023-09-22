# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Funcao que recebe uma str e insere "#" no inicio, meio e fim
    str -> str'''
    r1 = s[:len(s)//2:]
    r2 = s[len(s)//2:]
    return str("#") + r1 + str("#") + r2 + str("#")