# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(x):
    '''
    Função que recebe uma string e inclui três hashtags,um no inicio, outro no meio
    e o último no final da string.
    str-->str
    '''
    palavra = len(x)//2
    return ('#' + x[:palavra] + '#' + x[palavra:] + '#')