# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    '''função que retorna a concatenação de a e b no formato abba
    casos de teste:
    concatenacao('a','b') == 'abba'
    concatenacao('x','y') == 'xyyx'
    '''
    return a+b*2+a