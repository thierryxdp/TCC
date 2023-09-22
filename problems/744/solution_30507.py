# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """ Hashtag é uma função que recebe uma string e insere um "#" no inicio. meio e fim"""
    l=round(len(s)+-0.1/2)
    return "#" + s[:l] + "#" + s[l:] + "#"