# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função recebe uma string ''s'' e adiciona o caractere '#' no
    início, no meio e no fim da string.'''
    m = len(s) // 2
    return '#' + s[:m] + '#' + s[m:] + '#'