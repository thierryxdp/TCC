# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''dada a string, ele retorna a mesma com '#' no inicio, meio e fim; string -> str'''
    return '#'+s[:len(s)//2:]+'#'+s[len(s)//2:]+'#'