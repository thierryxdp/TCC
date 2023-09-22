# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ''' Função que coloca hashtag no inicio, no meio e no final de uma string dada
    str->str'''
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s