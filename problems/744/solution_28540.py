# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que recebe uma string e insere o caractere "#" no início,
    no meio e no final dessa string
    str -> str'''
    x = (len(s))/2
    y = int(x)
    return '#' + s[:y] + '#' + s[y:] + '#'