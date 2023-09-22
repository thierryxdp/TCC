# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que recebe uma string e insira o caractere # no ínicio, no meio e no final da string
    string, string, string -> string'''
    n = (len(s)//2)
    return '#'+s[0:n]+'#'+s[n:]+'#'