# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    '''Retorna a concatenação das strings a e b no formato abba;
    assinatura: str, str --> str
    Casos de teste:
    concatenacao('x', 'y') == 'xyyx'
    concatenacao('São', 'Paulo') == 'SãoPauloPauloSão'
    concatenacao('papel', 'toalha') == 'papeltoalhatoalhapapel'
    '''
    return str(a) + str(b) + str(b) + str(a)