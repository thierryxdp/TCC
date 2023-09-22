# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que recebe uma string e adiciona o caractere
    '#' no início, no meio e no final dela
    str -> str'''
    comprimento_s = len(s)
    meio = comprimento_s//2
    return '#' + s[0: meio] + '#' + s[meio + 1:] + '#'