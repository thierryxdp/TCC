# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que recebe uma string (s), e insere no início, no meio e no fim dela o caracter #'''
    string = s
    dividir = len(string)//2
    hashtag = '#'
    return hashtag+string[0:dividir]+hashtag+string[dividir:]+hashtag