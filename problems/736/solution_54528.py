# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    '''Retorna a concatenação dos valores inseridos, sendo a
    segunda justaposição feita de modo invertido (ab -> abba)
    str -> str'''
    return str(a)+str(b)+str(b)+str(a)