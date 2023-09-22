# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Essa função devolve a palavra selecionada com a string '#' no início, no meio e no final da palavra
    str -> str'''
    var = str(s)
    x = len(str(s))//2
    return '#' + var[:(x)] + '#' + var[(x):] + '#'