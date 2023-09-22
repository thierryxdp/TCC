# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ''' Função que acrescenta uma hashtag no inicio meio e final entre as strings; str->str'''
    return '#' +s[:len(s)//2]+'#'+s[len(s)//2:]+'#'