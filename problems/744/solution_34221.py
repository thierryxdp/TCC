# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Funcao que recebe uma string e retorna uma nova string contendo o caractere"#' no inicio,meio e fim da string.str->str'''
    i=len(s)
    i2=int(len(s)/2)
    s1='#'+s[:i2]+'#'+s[i2:]
    return s1