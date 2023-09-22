# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Retorna a string 's' de entrada com o caractere '#'
    inserido em seu início, meio e fim;
    str -> str'''
    tam=len(s)
    posMeio=len(s)//2
    return '#'+s[:posMeio]+'#'+s[posMeio:]+'#'