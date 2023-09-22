# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que recebe uma string e insere o caractere ''#''
    no ínicio, no meio e no final dela'''
    a = len(s)//2
    return '#' + s[:a] + '#' + s[a:] + '#'