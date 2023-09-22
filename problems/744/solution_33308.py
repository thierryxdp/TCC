# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Funcao que recebe um texto string e retorna uma nova string contendo '#' no começo, meio e fim da string de entrada;str->str'''
    m=(len(s))//2
    return s[:0]+'#'+s[m]+'#'+s[2:]+'#'