# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que recebe uma string e insere o caractere '#' no inicio,
    no meio e no final dela'''
    a = len(s)//2
    return '#'+s[:a:1]+'#'+ s[a:]+'#'