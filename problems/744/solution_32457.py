# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Insere # no inicio meio e fim da string (s) e lhe retorna
    str -> str'''
    middle_index = int(len(s)/2)
    return "#" + s[:middle_index] + '#' + s[middle_index:] + '#'