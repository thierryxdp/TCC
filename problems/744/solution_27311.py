# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(x):
    '''Função que recebe uma string (x) e insere # no início, no meio e no final
    da string. Entrada: str. Saída: str'''
    comp=len(x)
    return '#'+x[:comp//2]+ '#' + x[comp//2:]+'#'