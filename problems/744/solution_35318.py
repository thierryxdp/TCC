# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''funcao que recebe uma string e insere "#" no inicio, no meio e no final dela
    str->str'''
    return "#" + s[:(len(s)//2] + "#" + s[(len(s)//2:] + "#"