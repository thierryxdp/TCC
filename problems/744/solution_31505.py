# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Retorna a string com um # no início, meio e fim.'''
    m = len(s)//2
    novo_s = "#" + [0:4] + "#" + [4:] + "#"
    return novo_s