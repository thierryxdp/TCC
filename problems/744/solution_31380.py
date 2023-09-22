# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    funcao que recebe uma string e insere um caracter '#' no inicio
    no meio e no fim da string
    param:
    string - s
    caracter '#' - string
    retorna - string
    '''
    meio = len(s)//2
    return '#' + s[:meio] + '#' + s[meio+1:] + '#'