# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    '''---'''
    a = a + a[:]
    b = b + b[::-1]
    return a + b