# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que recebe uma string e inseri o caractere '#' no ínicio
    ,no meio e no final dela'''
    x=len(s)//2
    return '#'+s[:x]+'#'+s[x:]+'#'