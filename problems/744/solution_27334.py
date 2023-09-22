# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que recebe uma string e insere uma hashtag no início, meio e fim; str-> str'''
    return '#'+s[0:len(s)//2]+'#'+s[len(s)//2:]+'#'