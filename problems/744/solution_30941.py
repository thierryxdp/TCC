# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Recebe uma string e coloca uma # no começo meio e no fim da string'''
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s