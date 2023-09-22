# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''retorna o caractere '#' no ínicio, no meio e no final da string 's'; str -> str'''
    metade = len(s)//2
    return '#'+s[:metade]+'#'+s[metade:]+'#'