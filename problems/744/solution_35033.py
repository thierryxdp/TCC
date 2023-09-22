# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''recebe uma string (s) e insere o caractere'#' no inicio, meio e final dela;
    str->str'''
    return "#" + s[len(s)//2] + "#"