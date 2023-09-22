# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função recebe uma string e insere # no início, meio e fim dela'''
    return '#'+s[:len(s)//2:]+'#'+s[len(s)//2:]+'#'