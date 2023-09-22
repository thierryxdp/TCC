# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que recebe uma string (s), e insere no início, no meio e no fim dela o caracter #
    str -> str'''
    string = s
    dividir = len(string)//2
    hastag = '#'
    return hastag+string[0:dividir]+hastag+string[dividir:]+hastag