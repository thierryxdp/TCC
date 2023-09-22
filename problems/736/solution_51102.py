# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    '''função que retorna u,a string no formato abba, dadas as entradas a e b'''
    a = str(a)
    b = str(b)
    return (a+b)+(b+a)