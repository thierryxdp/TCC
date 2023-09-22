# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''a função pega a string dada em s e adiciona a string # no começo meio e no final da string dada em s'''
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s