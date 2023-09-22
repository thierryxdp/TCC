# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    '''Retorna a concatenação de duas strings a e b na ordem abba'''
    ab = str(a)+str(b)
    ba = str(b)+str(a)
    return ab+ba