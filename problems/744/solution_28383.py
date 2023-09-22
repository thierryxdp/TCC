# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''colocar hashatg no inicio, no meio e no final deuma string
str -> str'''
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s