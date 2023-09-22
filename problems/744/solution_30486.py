# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    A função retorna uma string a, escolhida pelo usuário,
    com o caractere "#" no início, no meio e no final
    (entrada = str / saída = str)
    '''
    return '#' + s[ : len(s) // 2] + '#' + s[len(s) // 2 : ] + '#'