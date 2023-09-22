# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(x):
    '''Dado uma string, insere o caractere '#'
    no início, no meio e no final da string.'''
    a = len(x)
    b = a//2
    return "#"+x[0:b]+'#'+x[b:]+'#'