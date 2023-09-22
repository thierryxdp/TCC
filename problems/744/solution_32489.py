# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Esta funcao insere um caractere no inicio, no meio e no final de uma string.'''
    '''str --> str'''
    antes = s[0:len(s)//2]
    depois = s[len(s) // 2 + 1:]
    return "#" + antes + "#" + depois + "#"