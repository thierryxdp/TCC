# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que receba uma string e insira o caractere "#" no início, no meio e no final dela.
    entrada: string
    saida: string'''
    x = len(s)//2
    return '#' + s[0:x] + '#' + s[x: ] + '#'