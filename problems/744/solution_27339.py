# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que recebe uma string e insira o
    caractere ”#” no início, no meio e no final dela'''
    m = len(s)//2
    return '#' + s[0:m] + '#' + s[m:] + '#'