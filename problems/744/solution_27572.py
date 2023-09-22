# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Insire o caractere "#" no início, meio e fim da string.
    str-> str'''
    meio = len(s)//2
    string2 = '#' + s[:meio] + '#' + s[meio:] + '#'
    return string2