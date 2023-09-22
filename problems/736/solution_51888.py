# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    '''Dadas as strings 'a' e 'b' a função retorna a concatenação das duas
       no formato abba
       str -> str
       Parametros:
       a: str a ser escolhida e digitada
       b: str a ser escolhida e digitada'''
    juncao1 = ''.join(a, b)
    juncao2 = ''.join(juncao1, b)
    return ''.join(juncao2, a)