# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    '''Essa função retorna a concatenação de 'a' e 'b' no formato abba
    str, str -> str'''
    a = str(a)
    b = str(b)
    return str(a) + str(b) + str(b) + str(a)