# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    ''' 
    Função recebe duas strings 'a' e 'b' e retornam a string 'abba'
    '''
    return str(a)+str(b)+str(b)+str(a)

a='a'; b='b'
concatenacao(a,b)