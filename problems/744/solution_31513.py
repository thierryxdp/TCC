# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(x):
    '''
    Função que recebe uma stringe inclui # no inicio, meio e no final da palavra.
    str --> str
    '''
    Palavra = len(x)//2
    return ('#' + x[:palavra] + '#' + x[palavra:] + '#')