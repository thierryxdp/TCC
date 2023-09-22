# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Recebe uma string e insere o caractere "#" no início, no meio e no final.
    str->str
    '''
    i=int((len(s)/2))
    return tup('#') + s[:i]+'#'+ s[i,] + tup('#')